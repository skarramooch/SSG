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

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "This is an image node")



if __name__ == "__main__":
    unittest.main()
