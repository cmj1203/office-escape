"""assets/office/_src 의 원본 그림을 게임용으로 줄여 assets/office 에 저장한다.

사용법: uv run --with pillow tools/process_sprites.py player.png enemy_mail.png floor_5f.png
"""

import sys
from pathlib import Path

from PIL import Image, ImageOps

OFFICE = Path(__file__).resolve().parent.parent / "assets" / "office"
SOURCE = OFFICE / "_src"
SPRITE_SIZE = 192
FLOOR_SIZE = 192
ALPHA_VISIBLE = 24
STORY_SIZE = (960, 640)
STORY_QUALITY = 86
# 보스 등장 연출용 큰 그림 (cutin_*): 화면에 크게 나오므로 크게 남긴다. 왼쪽을 보게 그려진 그대로 쓴다 (화면 오른쪽에서 들어옴).
CUTIN_SIZE = 640
# 게임은 "그림이 오른쪽을 본다"고 가정하고 필요할 때 뒤집는다. 보스 원본은 왼쪽을 보게 그려져서 여기서 미리 뒤집어 둔다.
FACES_LEFT_PREFIXES = ("boss_",)
# 층 전용 물건 (prop_*): 책상·회의 탁자처럼 옆으로 긴 것이 많아서 정사각형으로 채우지 않고 비율을 그대로 둔다. 긴 쪽이 이 크기
PROP_SIZE = 384
# 컷신 위에 크게 뜨는 휴대폰 그림 (phone_*): 물건처럼 비율 그대로, 긴 쪽이 이 크기
PHONE_SIZE = 768


def process_sprite(image: Image.Image, size: int = SPRITE_SIZE) -> Image.Image:
    alpha = image.getchannel("A").point(lambda a: 255 if a > ALPHA_VISIBLE else 0)
    box = alpha.getbbox()
    if box is None:
        raise ValueError("그림에 보이는 부분이 없다")
    cropped = image.crop(box)
    side = max(cropped.size)
    square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    square.paste(cropped, ((side - cropped.width) // 2, (side - cropped.height) // 2))
    return square.resize((size, size), Image.LANCZOS)


def process_prop(image: Image.Image, size: int = PROP_SIZE) -> Image.Image:
    alpha = image.getchannel("A").point(lambda a: 255 if a > ALPHA_VISIBLE else 0)
    box = alpha.getbbox()
    if box is None:
        raise ValueError("그림에 보이는 부분이 없다")
    cropped = image.crop(box)
    scale = size / max(cropped.size)
    return cropped.resize((round(cropped.width * scale), round(cropped.height * scale)), Image.LANCZOS)


def main(names: list[str]) -> int:
    for name in names:
        image = Image.open(SOURCE / name)
        is_floor = name.startswith("floor_") or name.startswith("wall")
        if name.startswith("story_"):
            result = image.convert("RGB").resize(STORY_SIZE, Image.LANCZOS)
            target = OFFICE / f"{Path(name).stem}.jpg"
            result.save(target, quality=STORY_QUALITY, optimize=True)
            print(f"{name}: {image.size[0]}x{image.size[1]} -> {target.name} {result.size[0]}x{result.size[1]}, {target.stat().st_size // 1024}KB")
            continue
        if name.startswith(("prop_", "phone_")):
            result = process_prop(image.convert("RGBA"), PHONE_SIZE if name.startswith("phone_") else PROP_SIZE)
            target = OFFICE / name
            result.save(target, optimize=True)
            print(f"{name}: {image.size[0]}x{image.size[1]} -> {result.size[0]}x{result.size[1]}, {target.stat().st_size // 1024}KB")
            continue
        if name.startswith("cutin_"):
            result = process_sprite(image.convert("RGBA"), CUTIN_SIZE)
            target = OFFICE / name
            result.save(target, optimize=True)
            print(f"{name}: {image.size[0]}x{image.size[1]} -> {result.size[0]}x{result.size[1]}, {target.stat().st_size // 1024}KB")
            continue
        if is_floor:
            result = image.convert("RGB").resize((FLOOR_SIZE, FLOOR_SIZE), Image.LANCZOS)
        else:
            result = process_sprite(image.convert("RGBA"))
            if name.startswith(FACES_LEFT_PREFIXES):
                result = ImageOps.mirror(result)
        target = OFFICE / name
        result.save(target, optimize=True)
        print(f"{name}: {image.size[0]}x{image.size[1]} -> {result.size[0]}x{result.size[1]}, {target.stat().st_size // 1024}KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
