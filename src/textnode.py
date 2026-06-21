from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "plain text"       # no tag
    BOLD = "bold text"         # **bold**
    ITALIC = "italic text"     # _italic_
    CODE = "code text"         # 'code'
    LINK = "link"            # [anchor text](url)
    IMAGE = "image"          # ![alt text](url)

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url= url

    def __eq__(self, other):
        #print(f"[eq called] self = {self} other = {other}")
        if self.text_type == other.text_type:
            if self.text == other.text:
                if self.url == other.url:
                    return True

    def __repr__(self):
         return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, text_node.url)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, text_node.url)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, text_node.url)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, text_node.url)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, text_node.url)
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", text_node.url)

    else:
        raise Exception("no chukka chukka")

# TextType.LINK: "a" tag, anchor text, and "href" prop
# TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    
