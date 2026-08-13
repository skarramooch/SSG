#done# Split the markdown into blocks (you already have a function for this)
#done# Loop over each block:
 #done# Determine the type of block (you already have a function for this)
#    Based on the type of block, create a new HTMLNode with the proper data
#    Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
#    The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node

from splitter import markdown_to_blocks, block_to_block_type, block, text_to_textnodes, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node

def markdown_to_html_node(whole_markdown_doc):
    md_blocks = markdown_to_blocks(whole_markdown_doc) #splits whole_md_doc into block chunks
    for md_block in md_blocks:
        md_Block = block(md_block)
        md_Block.block_type = block_to_block_type(md_block)
        md_Block_html = block_html_wrapper(md_Block)
        print(f"[md_Block_html] {md_Block_html}")




def block_html_wrapper(md_Block):
    if md_Block.block_type == BlockType.CODE:
        #send to special processor
        return codeblock_to_leafnode(md_Block)
    
    if md_Block.block_type == BlockType.PARA:
        block_children = text_to_children(md_Block.blocktext)
        return ParentNode("p", children=block_children)

    if md_Block.block_type == BlockType.HEAD:
        #print(f"[text_to_children] blocktype = HEAD")
        return

    if md_Block.block_type == BlockType.QUOT:
        #print(f"[text_to_children] blocktype = QUOT")
        return

    if md_Block.block_type == BlockType.UNOR:
        children = md_Block.blocktext.split("- ")
        html_block = ParentNode("ul", children)
        return html_block

    if md_Block.block_type == BlockType.ORDE:
        children = md_Block.blocktext.split(".") ##this isnt right, i think we need regex
        html_block = ParentNode("ol", children)
        return
        
    else:
        print(f"\n[AAARGH] {md_Block.block_type} didnt work\n")
    return md_Block





def codeblock_to_leafnode(md_Block):
    code_leaf_text = md_Block.blocktext[3:-3]
    return LeafNode("blockquote", code_leaf_text)

def text_to_children(text):
    # feed in lines of text which will be processed inline
    # p doesnt need it but it can come through
    # ul, ol, h1-6 can all come in here
    textnodes = text_to_textnodes(text)
    html_children = []
    for textnode in textnodes:
        html_child = text_node_to_html_node(textnode)
        html_children.append(html_child)
    return html_children

    
