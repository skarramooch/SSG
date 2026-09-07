from textnode import TextNode, TextType
from static_to_public import copy_static_to_public

def main():
    print(f"[main called]")
    skibbidy = TextNode("anchor text goes here", TextType.BOLD, "www.skarramooch.zapto.org")
    print(f"[main called] skibbidy is {skibbidy}")
    print(f"[main called] skibbidy text is {skibbidy.text}")
    print(f"[main called] skibbidy text_type is {skibbidy.text_type}")
    print(f"[main called] skibbidy url is {skibbidy.url}")
    print(skibbidy)
    copy_static_to_public("static", "public")

main()
