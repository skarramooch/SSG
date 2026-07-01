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
        #self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        #self.assertNotEqual(result, [node])
 


    def test_italic(self):
        #print("testing italic *")
        node = TextNode("This is an *italic* node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        #self.assertEqual(result, [node])
 


    def test_code(self):
        #print("testing code `")
        node = TextNode("This is a `code` node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        #self.assertEqual(result, [node])
 
    def test_delimiter(self):
        #print("testing delimiter xyz")
        node = TextNode("This is a xyznodexyz", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "xyz", TextType.BOLD)
        #self.assertEqual(result, [node])

    def test_delimiter_at_end(self):
        #print("testing delimiter at end")
        node = TextNode("This is a *node*", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        #self.assertEqual(resul, [node])
 
    def test_xyz_before_end(self):
        #print("testing delimiter xyz with text after")
        node = TextNode("This is a xyznodexyz with text after", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        #self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "xyz", TextType.BOLD)
        #self.assertEqual(result, [node])



    def test_unmatched(self):
        #print("testing unmatched delimiter")
        node = TextNode("This is a an *unmatched node", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.BOLD)

    def test_multiple_delimiters(self):
        node = TextNode("This has *multiple* *delimiters*", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        print(f"testing multiple delimiters, result[0].text: ({result[0].text})")
        print(f"testing multiple delimiters, result[1].text: ({result[1].text})")
        print(f"testing multiple delimiters, result[2].text: ({result[2].text})")
        print(f"testing multiple delimiters, result[3].text: ({result[3].text})")



        self.assertEqual(str(result[2].text), " ")

def test_multiple_nodes(self):
        node = TextNode("This is the *first* line", TextType.TEXT)
        node1 = TextNode("This is the *second* line", TextType.TEXT)
        node2 = TextNode("This is the third line (with no formatting)", TextType.TEXT)
        node3 = TextNode("This is the fourth (*last*) line", TextType.TEXT)

        html_node = text_node_to_html_node(node)
        html_node1 = text_node_to_html_node(node1)
        html_node2 = text_node_to_html_node(node2)
        html_node3 = text_node_to_html_node(node3)

        old_nodes = [node, node1, node2, node3]

        result = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)



