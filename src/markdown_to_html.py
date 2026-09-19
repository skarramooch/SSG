#done# Split the markdown into blocks (you already have a function for this)
#done# Loop over each block:
 #done# Determine the type of block (you already have a function for this)
#    Based on the type of block, create a new HTMLNode with the proper data
#    Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
#    The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node

from splitter import markdown_to_blocks, block_to_block_type, block, text_to_textnodes, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node, TextNode, TextType


def extract_title(markdown):
    print(f"[extract_title] markdown:\n{markdown}\n")
    # It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    # If there is no h1 header, raise an exception.
    # extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)
    first_line = markdown.splitlines()[0]
    if first_line.startswith("# "):
        header = first_line.split("# ", 1)[1]
        return header
    else:
        raise exception("first line did not start with H1")

def generate_page(from_path, template_path, dest_path):
    print(f"[generate_page] from_path {from_path}")
    print(f"[generate_page] template_path {template_path}")
    print(f"[generate_page] dest_path {dest_path}")
# Print a message like "Generating page from from_path to dest_path using template_path".
# Read the markdown file at from_path and store the contents in a variable.
# Read the template file at template_path and store the contents in a variable.
# Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
# Use the extract_title function to grab the title of the page.
# Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
# Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding="utf8") as f:
        markdown = f.read()
    print(f"[from file read and closed successfully] {f.closed}")
    with open(template_path, 'r', encoding="utf8") as t:
        template = t.read()
    print(f"[template file read and closed successfully] {t.closed}")
    print(f"files opened")
    html_node = markdown_to_html_node(markdown)
    print(f"\n[html node] \n{html_node}")
    html_string = html_node.to_html()
    print(f"\n[html string] \n{html_string}")
    title = extract_title(markdown)
    print(f"\n[title] \n{title}")
    template.replace("{{ Title }}", title)
    template.replace("{{ Content }}", html_string)
    print(f"\n[full html file]\n{template}\n")


def markdown_to_html_node(whole_markdown_doc):
    md_blocks = markdown_to_blocks(whole_markdown_doc) #splits whole_md_doc into block chunks
    htmlnode_blocks = []
    for md_block in md_blocks:
        #print(f"md_block = block(md_block)")
        #print(f"[md_block] = {repr(md_block)}")
        #print(f"md_Block.block_type = {block_to_block_type(md_block)}")
        md_Block = block(md_block)
        md_Block.block_type = block_to_block_type(md_block)
        md_Block_html = block_html_wrapper(md_Block)
        #print(f"[md_Block_html] {repr(md_Block_html)}\n\n")
        htmlnode_blocks.append(md_Block_html)
    return ParentNode("div", htmlnode_blocks)





def block_html_wrapper(md_Block):
    if md_Block.block_type == BlockType.CODE: ## DONE
        #send to special processor
        return codeblock_to_leafnode(md_Block)
    
    if md_Block.block_type == BlockType.PARA: ## DONE ##corrected inline breaks
        un_line_broken = md_Block.blocktext.replace("\n", " ") # swap newlines for spaces
        md_Block.blocktext = un_line_broken # reassign for cleanliness
        block_children = text_to_children(md_Block.blocktext)
        return ParentNode("p", children=block_children)

    if md_Block.block_type == BlockType.HEAD: ## DONE
        block_line = md_Block.blocktext
        level = 0
        for i in range(0,6):
            if block_line[0] == "#":
                level += 1
                block_line = block_line[1:]
        html_line = ParentNode(f"h{level}", text_to_children(block_line.strip()))
        return html_line

    if md_Block.block_type == BlockType.QUOT: ## DONE
        block_lines = md_Block.blocktext.splitlines()
        quote_lines = "" 
        for line in block_lines:
            stripped_quote_line = line[1:].strip()
            if stripped_quote_line != "":
                quote_lines += stripped_quote_line + " "
        quotepara = quote_lines.strip()
        quotetext = text_to_children(quotepara)
        html_block = ParentNode("blockquote", quotetext)
        return html_block


    if md_Block.block_type == BlockType.UNOR: ## DONE
        block_lines = md_Block.blocktext.splitlines()
        html_lines = []
        for line in block_lines:
            html_line = text_to_children(line[2:].strip())
            html_lines.append(ParentNode("li", html_line))
        html_block = ParentNode("ul", html_lines)
        return html_block

    if md_Block.block_type == BlockType.ORDE: ## DONE
        block_lines = md_Block.blocktext.splitlines()
        html_lines = []
        for prefixed_line in block_lines:
            line = prefixed_line.split(". ", 1)
            html_line = text_to_children(line[1].strip())
            html_lines.append(ParentNode("li", html_line))
        html_block = ParentNode("ol", html_lines)
        return html_block

        
    else:
        print(f"\n[AAARGH] {md_Block.block_type} didnt work\n")
    return md_Block





def codeblock_to_leafnode(md_Block):
    code_leaf_text = md_Block.blocktext.strip()[3:-3].lstrip("\n")
    code_leaf_text_node = TextNode(code_leaf_text, TextType.TEXT)
    code_leaf_html_node = text_node_to_html_node(code_leaf_text_node)
    return ParentNode("pre", [ParentNode("code", [code_leaf_html_node])])

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

    
