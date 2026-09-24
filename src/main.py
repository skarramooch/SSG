from sys import argv
from textnode import TextNode, TextType
from static_to_public import copy_static_to_public
from markdown_to_html import generate_pages_recursive

def main():
    if argv[0] is None:
        basepath = "/"
    else:
        basepath = argv[0].rsplit("src/main.py", 1)[0]
        if basepath == "":
            basepath = "/"
    print(f"[basepath] {basepath}")
    copy_static_to_public("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
