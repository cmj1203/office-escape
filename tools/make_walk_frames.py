"""걷기 시트(assets/office/_src/sheet_<이름>_walk.png, 마젠타 배경에 가로 4칸)를 게임용 프레임 4장으로 만든다.

사용법: uv run --with pillow tools/make_walk_frames.py player enemy_mail
  1) sprite-gen 의 cutout 으로 시트 전체의 마젠타 배경을 지운다 (외곽선에 번진 분홍기까지 정리)
  2) 투명한 세로줄을 경계로 그림 덩어리 4개를 찾고(떨어진 효과선은 가까운 덩어리에 합침), 네 장을 같은 높이·같은 배율로
     192px 정사각형에 넣는다 → 시트에 그려진 크기와 발 위치가 그대로 유지되어 걸을 때 몸이 커졌다 작아졌다 하지 않는다
  결과: assets/office/<이름>.png (1번 칸 = 서 있는 기본 그림. 예전 것은 _old/<이름>.before-walk.png 로) + <이름>_walk2.png ~ _walk4.png
sprite-gen 은 ~/sprite-gen 에 설치되어 있어야 한다 (SPRITE_GEN_ROOT 로 바꿀 수 있음).
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

OFFICE = Path(__file__).resolve().parent.parent / "assets" / "office"
SOURCE = OFFICE / "_src"
OLD = OFFICE / "_old"
SPRITE_GEN = Path(os.environ.get("SPRITE_GEN_ROOT", Path.home() / "sprite-gen"))
FRAMES = 4
SPRITE_SIZE = 192
ALPHA_VISIBLE = 24


def cut_background(sheet: Path, out: Path) -> Image.Image:
    subprocess.run(
        [str(SPRITE_GEN / ".venv" / "bin" / "sprite-gen"), "cutout", str(sheet), "--out", str(out), "--key", "magenta", "--decontam", "auto"],
        check=True, capture_output=True,
    )
    return Image.open(out).convert("RGBA")


def column_runs(visible: Image.Image) -> list[list[int]]:
    filled = [visible.crop((x, 0, x + 1, visible.height)).getbbox() is not None for x in range(visible.width)]
    runs: list[list[int]] = []
    for x, on in enumerate(filled):
        if on and runs and runs[-1][1] == x:
            runs[-1][1] = x + 1
        elif on:
            runs.append([x, x + 1])
    return runs


def split_cells(sheet: Image.Image) -> list[Image.Image]:
    visible = sheet.getchannel("A").point(lambda a: 255 if a > ALPHA_VISIBLE else 0)
    runs = column_runs(visible)
    if len(runs) < FRAMES:
        raise ValueError(f"그림 덩어리가 {len(runs)}개뿐이다 (칸끼리 붙어 있음: 시트를 다시 만들 것)")
    while len(runs) > FRAMES:
        gaps = [runs[i + 1][0] - runs[i][1] for i in range(len(runs) - 1)]
        i = gaps.index(min(gaps))
        runs[i:i + 2] = [[runs[i][0], runs[i + 1][1]]]
    top, bottom = visible.getbbox()[1], visible.getbbox()[3]
    return [sheet.crop((x0, top, x1, bottom)) for x0, x1 in runs]


def main(names: list[str]) -> int:
    for name in names:
        sheet = SOURCE / f"sheet_{name}_walk.png"
        with tempfile.TemporaryDirectory() as tmp:
            cells = split_cells(cut_background(sheet, Path(tmp) / "cut.png"))
        side = max(max(cell.width for cell in cells), cells[0].height)
        base = OFFICE / f"{name}.png"
        if base.exists():
            base.replace(OLD / f"{name}.before-walk.png")
        for i, cell in enumerate(cells):
            square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
            square.paste(cell, ((side - cell.width) // 2, (side - cell.height) // 2))
            target = base if i == 0 else OFFICE / f"{name}_walk{i + 1}.png"
            square.resize((SPRITE_SIZE, SPRITE_SIZE), Image.LANCZOS).save(target, optimize=True)
        widths = "/".join(str(cell.width) for cell in cells)
        print(f"{sheet.name}: 그림 너비 {widths}, 높이 {cells[0].height} -> {name}.png + {name}_walk2~{FRAMES}.png {SPRITE_SIZE}px")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
