import unittest
from regex import extract_markdown_images, extract_markdown_links

class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "this is an image, should be equal  ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_not_links(self):
        matches = extract_markdown_links(
            "This is text with piccy. should not extract ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is linked text [my personal creation](https://skarramooch.zapto.org)"
        )
        self.assertListEqual([("my personal creation", "https://skarramooch.zapto.org")], matches)

    def test_extract_markdown_not_image(self):
        matches = extract_markdown_images(
            "This is another link [this shouldnt work](https://avalanche.zapto.org)"
        )
        self.assertListEqual([], matches)

    def test_extra_square_brackets(self):
        matches = extract_markdown_images(
            "This will have some extra brackets in the alt text [extra [brackets] here](https://bracketyfun.org)"
        )
        self.assertListEqual([("extra [brackets] here", "https://bracketyfun.org")], matches)



"""
    def test_link(self):
        node = regex("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.asserEqueal("link", )

    def test_image(self):
        node = TextNode("alt text for image", TextType.IMAGE, "https://imgur.com")


class TestTextNode(unittest.TestCase):

    def test_md_images(self):
        text = "alt text for image", TextType.IMAGE, "https://imgur.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props['src'], "https://imgur.com")
        self.assertEqual(html_node.props['alt'], "alt text for image")

text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
"""


if __name__ == "__main__":
     unittest.main()
