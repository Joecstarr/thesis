from typing import List
from pathlib import Path
from tqdm import tqdm

TEX_PATH = Path("./_build/exports")

START_TAG = "%  @@@-subfigure-start-@@@\n"

END_TAG = "%  @@@-subfigure-end-@@@\n"

REPLACEMENTS = [
    {
        "original": "\\begin{figure}[!htbp]\n",
        "replacement": "\\begin{subfigure}{0.5\\textwidth}\n",
    },
    {"original": "\\end{figure}\n", "replacement": "\\end{subfigure}\n\\hfill\n"},
]


def swap(line: str):
    for replacement in REPLACEMENTS:
        if line == replacement["original"]:
            return replacement["replacement"]
    return line
    ...


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

        all_start_pos = [i for i, x in enumerate(file_lines) if x == START_TAG]
        all_end_pos = [i for i, x in enumerate(file_lines) if x == END_TAG]

        if len(all_start_pos) == len(all_end_pos):
            for start_idx, end_idx in zip(all_start_pos, all_end_pos):
                for i in range(start_idx + 1, end_idx):
                    file_lines[i] = swap(file_lines[i])
                    ...
                file_lines[start_idx] = "\\begin{figure}\n\\centering\n"
                if file_lines[end_idx - 2].startswith("%  @@@label:"):
                    file_lines[end_idx - 2] = (
                        "\\caption[$\\,$]{$\\,$}\\label{"
                        + file_lines[end_idx - 2].replace("%  @@@label:", "").replace("\n","")
                        + "}"
                    )
                else:
                    file_lines[end_idx - 2] = "\\caption[$\\,$]{$\\,$}"
                file_lines[end_idx - 1] = ""
                file_lines[end_idx] = "\\end{figure}\n"
                ...
        else:
            raise ValueError("Badness.")
        ...

        write(tex_file, file_lines)
