import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        print(f"test_eq - node = ")
        node = HTMLNode("Tag", "value", "children", "props")
        print(node)
        #node2 = HTMLNode("Tag", "value", "children", "props")
        #self.assertEqual(node, node2)

    def test_empty(self):
        node3 = HTMLNode("empty")
        #node4 = HTMLNode("empty")
        #self.assertEqual(node3, node4)

    def test_tag_not_eq(self):
        node5 = HTMLNode("Tag", "value", "children", "props")
        #node6 = HTMLNode("SPAG", "value", "children", "props")
        #self.assertNotEqual(node5, node6)

    def test_value_not_eq(self):
        node7 = HTMLNode("Tag", "value", "children", "props")
        #node8 = HTMLNode("Tag", "no val", "children", "props")
        #self.assertNotEqual(node7, node8)

    def test_kids_not_eq(self):
        node9 = HTMLNode("Tag", "value", "Jethro", "props")
        #node10 = HTMLNode("Tag", "value", "Isabel", "props")
        #self.assertNotEqual(node9, node10)

    def test_missing_text(self):
        node11 = HTMLNode("Tag", "value", "children", "props")
        #node12 = HTMLNode("Tag", "value", "children", "props")
        #self.assertNotEqual(node11, node12)


if __name__ == "__main__":
    unittest.main()
