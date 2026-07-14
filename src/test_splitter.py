import unittest
from splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node #text_to_textnodes

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


    def test_text_after_link(self):
        node = TextNode(
            "Hello [site](url) world",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0], TextNode("Hello ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("site", TextType.LINK, "url"))
        self.assertEqual(new_nodes[2], TextNode(" world", TextType.TEXT))

    def dont_test_text_no_link(self):
        node = TextNode(
            "Hello site](url) world",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0], TextNode("Hello site](url) world", TextType.TEXT))
        self.assertNotEqual(new_nodes[1], TextNode("site", TextType.LINK, "url"))
        self.assertNotEqual(new_nodes[2], TextNode(" world", TextType.TEXT))

    def dont_test_no_text_before_link(self):
        node = TextNode(
            "[site](url) world",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertNotEqual(new_nodes[0], TextNode("Hello ", TextType.TEXT))
        self.assertEqual(new_nodes[0], TextNode("site", TextType.LINK, "url"))
        self.assertEqual(new_nodes[1], TextNode(" world", TextType.TEXT))

    def dont_test_no_link(self):
        node = TextNode(
            "hello world, **bold** _italic_`code`",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0], TextNode("hello world, **bold** _italic_`code", TextType.TEXT))

    def dont_test_multiple_links(self):
        node = TextNode(
            "Hello [site](url) world [other_site](otherurl) aftercheck",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0], TextNode("Hello ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("site", TextType.LINK, "url"))
        self.assertEqual(new_nodes[2], TextNode(" world", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("other_site", TextType.LINK, "otherurl"))
        self.assertEqual(new_nodes[4], TextNode(" aftercheck", TextType.TEXT))
####
    def dont_test_non_text_nodes(self):
        node = TextNode(
            "[site](url) world",
            TextType.BOLD,
            )
        new_nodes = split_nodes_link([node])
        self.assertNotEqual(new_nodes[0], TextNode("Hello ", TextType.TEXT))
        self.assertEqual(new_nodes[0], TextNode("site", TextType.LINK, "url"))
        self.assertEqual(new_nodes[1], TextNode(" world", TextType.TEXT))

    def dont_test_unchanged(self):
        node1 = TextNode(
            "Plain Text Node",
            TextType.TEXT,
            )
        node2 = TextNode(
            "BOLD TEXT NOTE",
            TextType.BOLD,
            )
         node3 = TextNode(
            "ITALIC NODE",
            TextType.ITALIC,
            )
        node4 = TextNode(
            "CODE NODE",
            TextType.CODE,
            )
        node5 = TextNode(
            "image ![alt_text](image_url) node",
            TextType.TEXT,
            )
        nodes = [node1, node2, node3, node4, node5]
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes[0], TextNode("Plain Text Node", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("BOLD TEXT NODE", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode("ITALIC NODE", TextType.ITALIC))
        self.assertEqual(new_nodes[3], TextNode("CODE NODE", TextType.CODE))
        self.assertEqual(new_nodes[4], TextNode("image ![alt_text](image_url) node", TextType.ITALIC))



######





    def dont_test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

# a node with no links/images should come back unchanged
# text before a match should be preserved
# text after a match should be preserved
# no text before and after should also be preserved
# multiple matches in one node should all be handled
# non-TEXT nodes should pass through unchanged
#

 

