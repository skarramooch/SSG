import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("Tag", "value", "children", "props")
        node2 = HTMLNode("Tag", "value", "children", "props")
        self.assertEqual(node1, node2)

    def test_empty(self):
        node3 = HTMLNode()
        node4 = HTMLNode(None, None, None, None)
        self.assertEqual(node3, node4)

    def test_not_none(self):
        node5 = HTMLNode("Tag", "value", "children", "props")
        assert node5.tag is not None
        assert node5.value is not None
        assert node5.children is not None
        assert node5.props is not None

    def test_props_to_html_single_prob(self):
        node6 = HTMLNode("a", "skarramooch.zapto.org", None, {"href": "https://skarramooch.zapto.org"})
        self.assertEqual(node6.props_to_html(), ' href="https://skarramooch.zapto.org"')

    def test_props_to_multiple_props(self):
        node7 = HTMLNode("a", "Boot.dev", None, {
            "href": "https://boot.dev",
            "target": "_blank",
        })
        result = node7.props_to_html()
        self.assertIn(' href="https://boot.dev"', result)
        self.assertIn(' target="_blank"', result)

    def test_props_to_html_no_props(self):
        node8 = HTMLNode("a", "No.props", None, None)
        self.assertEqual(node8.props_to_html(), "")

    def test_kids_not_eq(self):
        node9 = HTMLNode("Tag", "value", "Jethro", "props")
        node10 = HTMLNode("Tag", "value", "Isabel", "props")
        self.assertNotEqual(node9, node10)

    def test_repr_contains_fields(self):
        node11 = HTMLNode("p", "hello", [], {"class": "text"})
        result =repr(node11)
        self.assertIn("tag = p", result)
        self.assertIn("value = hello", result)
        self.assertIn("children = []", result)
        self.assertIn("props = {'class': 'text'}", result)

### leaf node tests

    def test_add_leafnode(self):
        node12 = LeafNode("p", "this is the text inside the paragrapha leaf node - no kids", "")

    def test_leaf_properties(self):
        node13 = LeafNode("p", "L123456F", "")
        self.assertEqual(node13.to_html(), "<p>L123456F</p>")

    def test_leaf_eq(self):
        node14 = LeafNode("p", "Am I Equal?", "")
        node15 = LeafNode("p", "Am I Equal?", "")
        self.assertEqual(node14, node15)

    def test_leaf_link(self):
        node16 = LeafNode("a", "checkout my website", {"href": "https://bigbum.com"})
        self.assertEqual(node16.to_html(), '<a href="https://bigbum.com">checkout my website</a>')

### parent node tests

    def test_add_parentnode(self):
        node = ParentNode("p", [], "")

    def test_valueerror(self):
        node = ParentNode("", [], "")
        self.assertRaises(ValueError)

    def test_no_children(self):
        node = ParentNode("a", None, "")
        self.assertRaises(ValueError)

    def test_children(self):
        jethro = LeafNode("p", "Jethro", "")
        isabel = LeafNode("p", "Isabel", "")
        parent = ParentNode("p", [jethro, isabel], "")
        self.assertEqual(parent.to_html(), '<p><p>Jethro</p><p>Isabel</p></p>')

    def test_boot_example(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node.to_html()
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
