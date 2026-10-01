"""그림 여러 장을 이름과 함께 한 장에 모아 본다 (검은 배경과 바닥색 배경을 번갈아 깔아 윤곽 확인).

사용법: uv run --with pillow tools/contact_sheet.py 결과.jpg 그림1.png 그림2.png ...
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw

CELL = 300
LABEL = 28
COLUMNS = 4
BACKGROUNDS = [(20, 20, 24), (44, 50, 66)]


def main(out: str, paths: list[str]) -> int:
    rows = (len(paths) + COLUMNS - 1) // COLUMNS
    sheet = Image.new("RGB", (COLUMNS * CELL, rows * (CELL + LABEL)), (0, 0, 0))
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(paths):
        left = (index % COLUMNS) * CELL
        top = (index // COLUMNS) * (CELL + LABEL)
        image = Image.open(path).convert("RGBA")
        image.thumbnail((CELL, CELL), Image.LANCZOS)
        cell = Image.new("RGBA", (CELL, CELL), BACKGROUNDS[index % 2] + (255,))
        cell.alpha_composite(image, ((CELL - image.width) // 2, (CELL - image.height) // 2))
        sheet.paste(cell.convert("RGB"), (left, top + LABEL))
        draw.text((left + 6, top + 8), Path(path).name, fill=(255, 255, 255))
    sheet.save(out, quality=88)
    print(f"{out}: {len(paths)} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1], sys.argv[2:]))
