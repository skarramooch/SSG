from textnode import TextType, TextNode
from regex import extract_markdown_images, extract_markdown_links, match_block_headings
import re
from enum import Enum

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
    result_after_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    result_after_italic = split_nodes_delimiter(result_after_bold, "_", TextType.ITALIC)
    result_after_code = split_nodes_delimiter(result_after_italic, "`", TextType.CODE)
    result_after_image = split_nodes_image(result_after_code)
    result_after_link = split_nodes_link(result_after_image)
    return result_after_link

def old_markdown_to_blocks(md):
    blocks = []
    splitted = md.split("\n\n")
    stripped = []
    for block in splitted:
        stripped.append(block.strip())
    for block in stripped:
        if block != '':
            if block[0] == "#":
                # print(f"[MD 2 blcks] [HEADER BLCOK FOUND] in block: \n\n***\n{block}\n***\n\n")
                header_split_blocks = block.split("\n", 1)
                for hs_block in header_split_blocks:
                    blocks.append(hs_block)
            else:
                blocks.append(block)
    return blocks

def oldtwo_markdown_to_blocks(md):
    md_lines = md.splitlines()
    blocks = []
    current_block = ""
    NOSPLIT = False
    for md_line in md_lines:
        is_fence_line = "```" in md_line
        print(f"A[is_fence_line]     {is_fence_line}, {md_line}")
        was_in_code_block = NOSPLIT
        print(f"B[was_in_code_block] {was_in_code_block}, {md_line}\n")
        if is_fence_line:
            NOSPLIT = not NOSPLIT
        if not was_in_code_block:
            print(f"[md_line] {md_line}")
            #stripped_md_line = md_line.strip()
            if md_line != "\n":
                current_block = current_block + md_line.strip() + "\n"
                print(f"C[fence {is_fence_line}][codeblk {was_in_code_block}]\n{current_block}")
            else:
                if current_block != "":
                    blocks.append(current_block.strip())
                    current_block = ""

                    print(f"D[fence {is_fence_line}][codeblk {was_in_code_block}]\n{current_block}")
        else:
            current_block = current_block + md_line + "\n"

            print(f"E[fence {is_fence_line}][codeblk {was_in_code_block}]\n{current_block}")
            if is_fence_line and was_in_code_block:
                blocks.append(current_block.strip())
                current_block = ""
    if current_block != "":
        blocks.append(current_block.strip())
    return blocks

def markdown_to_blocks(md):
    md_lines = md.splitlines()
    blocks = []
    final_blocks = []
    current_block = ""
    CODETEXT = False
    for md_line in md_lines:
        codefence_line = "```" in md_line
        codefence_closed = CODETEXT

    ## codeblock handling
    # coeblock start
    # codeblock finish
    # codeblock add and flush
        if codefence_line and not codefence_closed:

            # current line is start of codeblock
            # Check current_block is empty
            # toggle fenceclosed
            CODETEXT = not CODETEXT
            if current_block != "":
                # finish current block and start codeblock
                blocks.append(current_block.strip())
                current_block = md_line
            else:
                #just start new codeblock
                current_block = md_line
        if codefence_line and codefence_closed:
            # finish codeblock
            current_block += md_line
            blocks.append(current_block.strip())
            current_block = ""

    ## noncodeblock handling
    # current_block empty line check
    # add line to current block

        if current_block == "":
            current_block = md_line.strip()

    # non empty line
    # split on \n\n
        if md_line == "\n\n":
            blocks.append(current_block.strip())
    # check current block type
        line_type =  block_to_block_type(md_line)
    # check line type
    # if type is head make it a 1 line block!
        if line_type == "HEAD":
            blocks.append(current_block.strip())
            current_block = md_line

    # ?  if same
        if block_to_block_type(current_block) == block_to_block_type(md_line):
            #shoudl i do different building for each block type? I think so!
            # i think everything other than head is ok to match and continue block
            # add line to current block
                current_block = current_block + md_line.strip()

    # ? if different
        if block_to_block_type(current_block) != block_to_block_type(md_line):
            # else:
            # finish current block, 
            # add line to new block
            blocks.append(current_block.strip())
            current_block = md_line

    print(f"[complete blocks] {blocks}")

    # clean blocks
    for block in blocks:
        if block != "":
            final_blocks.append(block)
    return final_blocks





class BlockType(Enum):
    PARA = "paragraph"  # #paragraph
    HEAD = "heading"    # #heading
    CODE = "code"       # #code
    QUOT = "quote"      # #quote
    UNOR = "unordered"  # #unordered_list
    ORDE = "ordered"    # #ordered_list
    #NORM = "normal"

class block:
    def __init__(self, blocktext, block_type = None):
        self.blocktext = blocktext
        self.block_type = block_type

def block_to_block_type(md_block):
    md = block(md_block)
    #md.block_type == BlockType.NORM
    if  match_block_headings(md.blocktext):
        return BlockType.HEAD
    if md.blocktext.startswith("```") and md.blocktext.endswith("```"):
        return BlockType.CODE
    md_split = md.blocktext.split("\n")
    QUOTESUM = 0
    UNORDEREDSUM = 0
    ORDERSUM = 0
    for line in md_split:
        if line.startswith(">"):
            QUOTESUM += 1
        if line.startswith ("- "):
            UNORDEREDSUM += 1
    if QUOTESUM == len(md_split):
        return BlockType.QUOT
    if UNORDEREDSUM == len(md_split):
        return BlockType.UNOR
    for n in range(1, len(md_split) + 1):
        if md_split[n-1].startswith(f"{str(n)}. "):
            ORDERSUM += 1
    if ORDERSUM == len(md_split):
        return BlockType.ORDE

    if md is not None:
        md.block_type = BlockType.PARA
    return md.block_type

 
# Headings start with 1-6 # characters, followed by a space and then the heading text.
# Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
# Every line in a quote block must start with a "greater-than" character: > followed by the quote text. A space after > is allowed but not required.
# Every line in an unordered list block must start with a - character, followed by a space.
# Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
# If none of the above conditions are met, the block is a normal paragraph.
