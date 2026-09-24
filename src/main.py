from sys import argv
from textnode import TextNode, TextType
from static_to_public import copy_static_to_public
from markdown_to_html import generate_pages_recursive

def main():
    if argv[1] is None:
        basepath = "/"
    else:
        basepath = argv[1] + "/"
    print(f"[basepath] {basepath}")
    copy_static_to_public("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
