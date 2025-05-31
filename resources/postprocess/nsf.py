from typing import List
from pathlib import Path
from tqdm import tqdm

TEX_PATH = Path("./_build/exports")

REPLACEMENTS = [
    {
        "original": "Remark",
        "replacement": "Algorithm",
    },
    {
        "original": "Observation",
        "replacement": "Figure",
    },
]


def read(file: Path):
    file_lines = []
    with open(str(file), "r") as texfile:
        while line := texfile.readline():
            file_lines.append(line)
    return file_lines


def write(file: Path, lines: List):
    with open(str(file), "w") as texfile:
        texfile.writelines(lines)


if __name__ == "__main__":
    for tex_file in tqdm(list(TEX_PATH.glob("**/*.tex"))):
        file_lines = read(tex_file)
        for i, line in enumerate(file_lines):
            for replace in REPLACEMENTS:
                file_lines[i] = file_lines[i].replace(
                    replace["original"], replace["replacement"]
                )
        write(tex_file, file_lines)
