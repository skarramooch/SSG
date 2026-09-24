from splitter import markdown_to_blocks, block_to_block_type, block, text_to_textnodes, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node, TextNode, TextType
from os import listdir,mkdir
from os.path import exists, isdir, isfile

def extract_title(markdown):
    first_line = markdown.splitlines()[0]
    if first_line.startswith("# "):
        header = first_line.split("# ", 1)[1]
        return header
    else:
        raise exception("first line did not start with H1")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} on basepath {basepath}")
    with open(from_path, 'r', encoding="utf8") as f:
        markdown = f.read()
    with open(template_path, 'r', encoding="utf8") as t:
        template = t.read()
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    title = extract_title(markdown)
    # reading files
    t_template = template.replace("{{ Title }}", title)
    f_t_template = t_template.replace("{{ Content }}", html_string)
    h_f_t_template = f_t_template.replace('href="/', f'href="{basepath}')
    s_h_f_t_template = h_f_t_template.replace('src="/', f'src="{basepath}')
    full_file = s_h_f_t_template

    # file structure
    dest_path_list = dest_path.split("/")
    dest_path_folder = dest_path_list[0]
    if not exists(dest_path_folder):
        mkdir(dest_path_folder)
    for n in range(1, len(dest_path_list) - 1):
        dest_path_folder = dest_path_folder + "/" + dest_path_list[n]
        if not exists(dest_path_folder):
            mkdir(dest_path_folder)
        # else:
            # print(f"[gen page] dest_path_folder already exists: {dest_path_folder}")
    with open(dest_path, 'w', encoding="utf8") as j:
        j.write(full_file)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # explore contect path
    # when file found, generate_page
    dir_list = listdir(dir_path_content)
    for folder in dir_list:
        folder_path = dir_path_content + "/" + folder
        if isdir(folder_path):
            generate_pages_recursive(folder_path, template_path, dest_dir_path + "/" + folder, basepath)
        else:
            filename = folder.rsplit(".md", 1)[0]
            generate_page(folder_path, template_path, dest_dir_path + "/" + filename + ".html", basepath)

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

    
