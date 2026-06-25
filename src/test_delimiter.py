import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node

class TestDelimiter(unittest.TestCase):
    def test_none(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "_", TextType.TEXT)
        self.assertEqual(result, [node])
        
    def test_bold(self):
        #print("testing bold **")
        node = TextNode("This is a **bold** node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "**", TextType.TEXT)
        self.assertNotEqual(result, [node])
 


    def test_italic(self):
        #print("testing italic *")
        node = TextNode("This is an *italic* node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "*", TextType.TEXT)
        self.assertEqual(result, [node])
 


    def test_code(self):
        #print("testing code `")
        node = TextNode("This is a `code` node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertEqual(result, [node])
 
    def test_delimiter(self):
        #print("testing delimiter xyz")
        node = TextNode("This is a xyznodexyz", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "xyz", TextType.TEXT)
        self.assertEqual(result, [node])
 
