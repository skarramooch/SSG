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

# PLAN
# use regex fns to split links and store in memory
# not sure how to split it out now
# maybe 

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    for node in old_nodes:
        print(f"\n[split_nodes_image node] {node}")
        print(f"[split_nodes_image node.text] {node.text }")
        new_images = extract_markdown_images(node.text)
        print(f"[split_nodes_image new_node] {new_images}")

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    for node in old_nodes:
        print(f"\n[split_nodes_link node] {node}")
        print(f"[split_nodes_link node.text] {node.text}")
        new_links = extract_markdown_links(node.text)
        print(f"[split_nodes_link new_node] {new_links}")
        for seg in new_links:
            print(f"[seg] {seg}")
            seg_alt = seg[0]
            seg_url = seg[1]
            print(f"[alt text] {seg_alt}")
            print(f"[url] {seg_url}")
