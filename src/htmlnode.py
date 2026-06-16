class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        print(f"[HTMLNode init] {tag}, {value}, {children}, {props}")
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise "NotImplementedError"

    def props_to_html(self):
        html = ""
        for prop in self.props:
            html += " " + prop
        return html

    def __repr__(self):
        return f"HTMLNode {self.value}: tag = {self.tag}, children = {self.children}, props = {self.props}"
