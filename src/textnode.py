from enum import Enum

class TextType(Enum):
    plain = "plain text"       # no tag
    bold = "bold text"         # **bold**
    italic = "italic text"     # _italic_
    code = "code text"         # 'code'
    links = "links"            # [anchor text](url)
    images = "images"          # ![alt text](url)

class TextNode:
    def __init__(self, text, text_type, url=None):
        print(f"[TextNode init called] self, text = {text}, text_type = {text_type}, url = {url}")
        self.text = text
        self.text_type = text_type
        self.url= url

    def __eq__(self, other):
        if self.TextNode == other.TextNode:
            return True

    def __repr__(self):
         return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

