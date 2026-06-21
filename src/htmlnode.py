class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for prop in self.props:
            html += " " + prop + "=" + '"' + self.props[prop] + '"'
        return html

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode {self.value}: tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
    	super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'



    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
        )

    def __repr__(self):
        return f"LeafNode: tag = {self.tag}, value = {self.value}, props = {self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("you didn't supply any children")
        child_part = ""
        for child in self.children:
            child_part += child.to_html()
        result = f'<{self.tag}>{child_part}</{self.tag}>'
        return result
