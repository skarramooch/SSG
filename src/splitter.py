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
        subseg = []
        for seg in new_images:
            seg_alt = seg[0]
            seg_url = seg[1]
            subseg.append(node.text.split(f"[{seg_alt}]({seg_url})", 1))
            new_nodes.append(TextNode(f"{subseg[0].pop(0)}", TextType.TEXT))
            new_nodes.append(TextNode(f"!{seg_alt}", TextType.IMAGE, f"({seg_url})"))
            subseg.pop(0)
    print(new_nodes)
    return new_nodes
        
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        new_links = extract_markdown_links(node.text)
        subseg = []
        
        for seg in new_links:
            seg_alt = seg[0]
            seg_url = seg[1]
            subseg.append(node.text.split(f"[{seg_alt}]({seg_url})", 1))
            new_nodes.append(TextNode(f"{subseg[0].pop(0)}", TextType.TEXT))
            new_nodes.append(TextNode(f"{seg_alt}", TextType.LINK, f"{seg_url}"))
            subseg.pop(0)
    print(f"[new_nodes LINK] {new_nodes}")
    return new_nodes
