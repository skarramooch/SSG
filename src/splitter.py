from textnode import TextType, TextNode
from regex import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    bracket_queue = []
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            print(f"you should only see this if node.text_type!= TextType.TEXT : {node.text_type}")


        split_nodes = []
        frags = node.text.split(delimiter)
        if len(frags) % 2 == 0:
            raise ValueError("Invalid Markdown - odd number of delimiter sets")

        for f in range(len(frags)):
            if frags[f] == "":
                continue
            if f % 2 == 0:
                split_nodes.append(TextNode(frags[f], TextType.TEXT))
            else:
                split_nodes.append(TextNode(frags[f], text_type))
        new_nodes.extend(split_nodes)

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        new_images = extract_markdown_images(node.text)
        node_text = [node.text]
        for seg in new_images:
            seg_alt = seg[0]
            seg_url = seg[1]
            node_text = node_text[0].split(f"![{seg_alt}]({seg_url})", 1)
            if node_text[0] != '':
                new_nodes.append(TextNode(f"{node_text.pop(0)}", TextType.TEXT))
            else:
                node_text.pop(0)
            new_nodes.append(TextNode(f"{seg_alt}", TextType.IMAGE, f"{seg_url}"))
    return new_nodes
        
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        new_links = extract_markdown_links(node.text)
        node_text = [node.text]
        for seg in new_links:
            seg_alt = seg[0]
            seg_url = seg[1]
            node_text = node_text[0].split(f"[{seg_alt}]({seg_url})", 1)
            print(f"[node_text] {node_text}")
            if node_text[0] != '':
                new_nodes.append(TextNode(f"{node_text.pop(0)}", TextType.TEXT))
            else:
                node_text.pop(0)
            new_nodes.append(TextNode(f"{seg_alt}", TextType.LINK, f"{seg_url}"))
            print(f"[node_text] {node_text}")
 
            if node_text[0] != '':
                print(f"i need to preserve this: {node_text[0]}")
                new_nodes.append(TextNode(f"{node_text.pop(0)}", TextType.TEXT))
 
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    result_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    result_italic = split_nodes_delimiter(result_bold, "_", TextType.ITALIC)
    result_code = split_nodes_delimiter(result_italic, "`", TextType.CODE)
    result_image = split_nodes_image(result_code)
    result_link = split_nodes_link(result_image)
    print(f"****\n{result_link}\n****")
    return result_link
