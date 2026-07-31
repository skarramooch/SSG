#Split the markdown into blocks (you already have a function for this)
#Loop over each block:

#    Determine the type of block (you already have a function for this)
#    Based on the type of block, create a new HTMLNode with the proper data
#    Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
#    The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node

from splitter import markdown_to_blocks, block_to_block_type, block

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    print(f"blocks: {blocks}")
    for block in blocks:
        for seg in blocks:
            #print(f"[block[{b}]]: {blocks[b]}")
            html_node = process_block(seg)
        


def process_block(block):
    print(f"[process_block] block: {block}")
    blocktype = block_to_block_type(block)
    print(f"[process_block] blocktype: {blocktype}")
    htmlnode = block_and_type_to_html_node(block, blocktype)
    print(f"[process_block] htmlnode: {htmlnode}")
    return htmlnode


def block_and_type_to_html_node(block, blocktype):
    print(f"[block_and_type_to_html_node] block: {block}, blocktype {blocktype}")
    return '<html>node</html>'
