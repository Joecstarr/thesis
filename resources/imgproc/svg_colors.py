import lxml.etree as ET
import re
from pathlib import Path
from rich import print
from tqdm import tqdm

IMAGE_PATH = Path("./media")

# | Palette      | Hex
# | ------------ | ---------
# | Background   | `#282a36`
# | Current Line | `#44475a`
# | Selection    | `#44475a`
# | Foreground   | `#f8f8f2`
# | Comment      | `#6272a4`
# | Cyan         | `#8be9fd`
# | Green        | `#50fa7b`
# | Orange       | `#ffb86c`
# | Pink         | `#ff79c6`
# | Purple       | `#bd93f9`
# | Red          | `#ff5555`
# | Yellow       | `#f1fa8c`

COLOR_SWAPS = [
    {
        "name": "background",
        "start": [
            "#282a36",
            "#ECEFF4",
            "#ffffff",
            "#ffffff",
            "#F2F3F4",
        ],
        "end": "#FFFFFF",
    },
    {
        "name": "blue",
        "start": ["#1e90ff", "#5E81AC", "#A1CAF1", "#8be9fd", "#0074D9", "#0000ff"],
        "end": "#0074D9",
    },
    {
        "name": "comment",
        "start": ["#2E3440", "#6272a4", "#848482", "#AAAAAA"],
        "end": "#AAAAAA",
    },
    {
        "name": "foreground",
        "start": ["#000000", "#0c0c0c", "#4C566A", "#111111", "#222222", "#f8f8f2"],
        "end": "#111111",
    },
    {
        "name": "green",
        "start": ["#50fa7b", "#008856", "#A3BE8C", "#2ECC40", "#A3BE8C", "#A3BE8C"],
        "end": "#2ECC40",
    },
    {
        "name": "orange",
        "start": ["#D08770", "#F38400", "#deb887", "#FF851B", "#deb887", "#ffb86c"],
        "end": "#FF851B",
    },
    {
        "name": "teal",
        "start": ["#BF6199", "#E68FAC", "#ff79c6", "#ff79c6", "#39CCCC"],
        "end": "#39CCCC",
    },
    {
        "name": "purple",
        "start": ["#B48EAD", "#875692", "#bd93f9", "#bd93f9", "#bd93f9"],
        "end": "#B10DC9",
    },
    {
        "name": "red",
        "start": ["#BF616A", "#ff0000", "#BE0032", "#ff5555", "#ff5555"],
        "end": "#FF4136",
    },
    {
        "name": "selection",
        "start": ["#434C5E", "#848482", "#654522", "#DDDDDD", "#44475a"],
        "end": "#DDDDDD",
    },
    {
        "name": "yellow",
        "start": ["#EBCB8B", "#F3C300", "#FFDC00", "#f1fa8c", "#f1fa8c"],
        "end": "#FFDC00",
    },
]


def set_style(file_content: str):
    file_content = re.sub(r'(class=".*?")', r"", file_content)
    file_content = re.sub(r"(style=.*)", r'class="" \1', file_content)
    return file_content


def swap(file_content: str):
    styles = file_content.split(";")
    class_list = []
    for i, style in enumerate(styles):
        for swap_color in COLOR_SWAPS:
            for color in swap_color["start"]:
                if re.match(rf".*{color}.*", style):
                    if style.startswith("stroke"):
                        styles[i] = f"stroke:{swap_color['end']}"
                        class_list.append(f"stroke-{swap_color['name']}")
                    if (
                        re.match(rf".*{swap_color['end']}.*", style)
                        and f"stroke-{swap_color['name']}" not in class_list
                    ):
                        class_list.append(f"stroke-{swap_color['name']}")
                    if style.startswith("fill"):
                        styles[i] = f"fill:{swap_color['end']}"
                        class_list.append(f"fill-{swap_color['name']}")
                    if (
                        re.match(rf".*{swap_color['end']}.*", style)
                        and f"fill-{swap_color['name']}" not in class_list
                    ):
                        class_list.append(f"fill-{swap_color['name']}")
                    break
    return ";".join(styles), " ".join(class_list)
    ...


for image in tqdm(
    list(set(IMAGE_PATH.glob("**/*.svg")) - set(IMAGE_PATH.glob("**/dont_proc/*.svg")))
):
    file_text = ""
    try:
        dom = ET.parse(image)
    except Exception as e:
        print(f"Failed to parse {xml_file}")
        print(e)
    for tag in dom.xpath("//*[@style]"):
        new_sty, classes = swap(tag.attrib["style"])
        tag.attrib["style"] = new_sty
        tag.attrib["class"] = classes
        ...
    with open(str(image), "w") as ptfile:
        ptfile.write(ET.tostring(dom, pretty_print=True).decode("utf8"))
    ...
