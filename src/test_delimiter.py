import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node

class TestDelimiter(unittest.TestCase):
    def test_none(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        print(f"node added: {node}")
        html_node = text_node_to_html_node(node)
        print(f"converted to html node: {html_node}")
        self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "_", TextType.TEXT)
        print(f"ran through split nodes: {result}")
        self.assertEqual(result, [node])

