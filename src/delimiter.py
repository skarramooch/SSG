from textnode import TextType, TextNode


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
