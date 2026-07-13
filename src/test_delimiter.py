import unittest
from splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType, text_node_to_html_node

class TestDelimiter(unittest.TestCase):
    def test_none(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        result = split_nodes_delimiter([node], "_", TextType.TEXT)
        self.assertEqual(result[0].text, "This is a plain text node")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_bold(self):
        node = TextNode("This is a **bold** node", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertNotEqual(result[1].text_type, result[0].text_type)

    def test_italic(self):
        node = TextNode("This is an *italic* node", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(result[1].text_type, TextType.ITALIC)

    def test_code(self):
        node = TextNode("This is a `code` node", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
 
    def test_delimiter(self):
        node = TextNode("This is a xyznodexyz", TextType.TEXT)
        result = split_nodes_delimiter([node], "xyz", TextType.BOLD)
        self.assertEqual(result[1].text, "node")

    def test_delimiter_at_end(self):
        node = TextNode("This is a *node*", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(result[1].text, "node")
        self.assertEqual(result[1].text_type, TextType.BOLD)
 
    def test_xyz_before_end(self):
        node = TextNode("This is a xyznodexyz with text after", TextType.TEXT)
        resultxyz = split_nodes_delimiter([node], "xyz", TextType.BOLD)
        resultxy = split_nodes_delimiter([node], "xy", TextType.ITALIC)
        self.assertEqual(resultxyz[0].text, resultxy[0].text)
        self.assertNotEqual(resultxyz[1].text_type, resultxy[1].text_type)

    def test_unmatched(self):
        node = TextNode("This is a an *unmatched node", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.BOLD)

    def test_multiple_delimiters(self):
        node = TextNode("This has *multiple* *delimiters*", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(result[0].text, "This has ")
        self.assertEqual(result[1].text, "multiple")
        self.assertEqual(result[2].text, " ")
        self.assertEqual(result[3].text, "delimiters")

def test_multiple_nodes(self):
        node = TextNode("This is the *first* line", TextType.TEXT)
        node1 = TextNode("This is the *second* line", TextType.TEXT)
        node2 = TextNode("This is the third line (with no formatting)", TextType.TEXT)
        node3 = TextNode("This is the fourth (*last*) line", TextType.TEXT)
        old_nodes = [node, node1, node2, node3]
        result = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        self.assertEqual(4, len(result))
        self.assertEqual(result[0][0].text, "This is the ")
        self.assertEqual(result[0][0].text_type, TextType.TEXT) 
        self.assertEqual(result[1][1].text, "second")
        self.assertEqual(result[1][1].text_type, TextType.BOLD)
        self.assertEqual(result[4][4].text, ") line")


class TestSplitter(unittest.TestCase):
    def test_link_splitter(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0], TextNode("This is text with a link ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"))
        self.assertEqual(new_nodes[2], TextNode(" and ", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"))
 
    def test_link_splitter_blank_first_node(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertNotEqual(new_nodes[0], TextNode("", TextType.TEXT))
        self.assertEqual(new_nodes[0], TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"))
        self.assertEqual(new_nodes[1], TextNode(" and ", TextType.TEXT))
        self.assertEqual(new_nodes[2], TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"))
 


    def test_image_splitter(self):
        node = TextNode(
            "This is text with an image ![image](https://www.piccystore.com) and ![image](https://www.cartoonwarehouse.org.nz)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_blank_first_node(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_blank_alt_text(self):
        node = TextNode(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_incorrectly_formed_not_equal(self):
        node = TextNode(
            "incorrectly formed [image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertNotEqual(
            [
                TextNode("incorrectly formed ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )





