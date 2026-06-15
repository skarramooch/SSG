from textnode import TextNode, TextType

def main():
    print(f"[main called]")
    skibbidy = TextNode("anchor text goes here", TextType.bold, "www.skarramooch.zapto.org")
    #print(f"[main called] skibbidy is {skibbidy}")
    print(f"[main called] skibbidy text is {skibbidy.text}")
    print(f"[main called] skibbidy text_type is {skibbidy.text_type}")
    print(f"[main called] skibbidy url is {skibbidy.url}")

main()
