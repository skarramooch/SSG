import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node3 = TextNode("textnodes are rad", TextType.ITALIC, "https://cabbcage.org")
        node4 = TextNode("textnodes suck", TextType.TEXT, "MALFORMEDURL")
        self.assertNotEqual(node3, node4)

    def test_text_not_eq(self):
        node5 = TextNode("TEXT", TextType.IMAGE)
        node6 = TextNode("text", TextType.IMAGE)
        self.assertNotEqual(node5, node6)

    def test_text_type_not_eq(self):
        node7 = TextNode("different types", TextType.LINK)
        node8 = TextNode("different types", TextType.TEXT)
        self.assertNotEqual(node7, node8)

    def test_url_not_eq(self):
        node9 = TextNode("diff URL", TextType.TEXT)
        node10 = TextNode("diff URL", TextType.TEXT, "ftp://ftp")
        self.assertNotEqual(node9, node10)

    def test_missing_text(self):
        node11 = TextNode("Missingtxt", TextType.BOLD)
        node12 = TextNode("", TextType.BOLD)
        self.assertNotEqual(node11, node12)

### test text-node-to-html-node

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
