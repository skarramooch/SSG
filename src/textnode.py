from enum import Enum

class TextType(Enum):
    PLAIN = "plain text"       # no tag
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

