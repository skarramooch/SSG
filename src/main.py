from textnode import TextNode, TextType
from static_to_public import copy_static_to_public
from markdown_to_html import generate_page

def main():
#    print(f"[main called]")
#    skibbidy = TextNode("anchor text goes here", TextType.BOLD, "www.skarramooch.zapto.org")
#    print(f"[main called] skibbidy is {skibbidy}")
#    print(f"[main called] skibbidy text is {skibbidy.text}")
#    print(f"[main called] skibbidy text_type is {skibbidy.text_type}")
#    print(f"[main called] skibbidy url is {skibbidy.url}")
#    print(skibbidy)
    copy_static_to_public("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md","template.html", "public/blog/glorfindel/index.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")


main()
