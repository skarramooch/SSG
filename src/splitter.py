from textnode import TextType, TextNode
from regex import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    bracket_queue = []
    new_nodes = []

    for node in old_nodes:
        split_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
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
    new_nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes_list.append(node)
        else:
            new_images = extract_markdown_images(node.text)
            remaining = node.text
            for seg in new_images:
                seg_alt = seg[0]
                seg_url = seg[1]
                before, remaining = remaining.split(f"![{seg_alt}]({seg_url})", 1)
                if before is not None and before != '':
                    new_nodes_list.append(TextNode(f'{before}', TextType.TEXT))
                new_nodes_list.append(TextNode(f"{seg_alt}", TextType.IMAGE, f"{seg_url}"))
            if remaining is not None and remaining != '':
                new_nodes_list.append(TextNode(f'{remaining}', TextType.TEXT))
    return new_nodes_list
        
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes_list.append(node)
        else:
            new_links = extract_markdown_links(node.text)
            remaining = node.text
            for seg in new_links:
                seg_alt = seg[0]
                seg_url = seg[1]
                before, remaining = remaining.split(f"[{seg_alt}]({seg_url})", 1)
                if before is not None and before != '':
                    new_nodes_list.append(TextNode(f'{before}', TextType.TEXT))
                new_nodes_list.append(TextNode(f'{seg_alt}', TextType.LINK, f'{seg_url}'))

            if remaining is not None and remaining != '':
                new_nodes_list.append(TextNode(f'{remaining}', TextType.TEXT))
    return new_nodes_list

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    result_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    result_italic = split_nodes_delimiter(result_bold, "_", TextType.ITALIC)
    result_code = split_nodes_delimiter(result_italic, "`", TextType.CODE)
    result_image = split_nodes_image(result_code)
    result_link = split_nodes_link(result_image)
    return result_link

def markdown_to_blocks(md):
    blocks = []
    newline_split_md = md.strip().split("\n\n")
    for block in newline_split_md:
        if block != '':
            blocks.append(block)
    return blocks


