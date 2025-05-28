import lxml.etree as ET
from pathlib import Path
from rich import print
from tqdm import tqdm
import typer


def main(search_dir: str):
    for image in tqdm(list(Path(search_dir).glob("**/*.svg"))):
        try:
            dom = ET.parse(image)
        except Exception as e:
            print(f"Failed to parse {image}")
            print(e)

        for tag in dom.xpath(
            "//svg:text[@xml:space]",
            namespaces={
                "svg": "http://www.w3.org/2000/svg",
                "xml": "http://www.w3.org/XML/1998/namespace",
            },
        ):
            del tag.attrib["{http://www.w3.org/XML/1998/namespace}space"]
            ...

        with open(str(image), "w") as ptfile:
            ptfile.write(ET.tostring(dom, pretty_print=True).decode("utf8"))
        ...


if __name__ == "__main__":
    typer.run(main)
