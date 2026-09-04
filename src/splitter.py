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

def markdown_to_blocks(md):
    blocks = md.split("\n\n")
    non_empty_blocks = []
    for block in blocks:
        if block.strip() != "":
            non_empty_blocks.append(block.strip())
    return non_empty_blocks

### below is 3 weeks of wasted time trying to do a line by line md2blks function.
### I can complete this after I have had therapy!!
def markdown_to_blocks_fence_aware_not_working(md):
    md_lines = md.splitlines()
    blocks = []
    final_blocks = []
    current_block = ""
    CODETEXT = False
    for md_line in md_lines:
        # check current block type
        line_type =  block_to_block_type(md_line)
        codefence_line = "```" in md_line
        codefence_closed = CODETEXT
        print(f"\n[A] {len(blocks)}")
        print(f"[A checks]\n[md_line]          ****** ({md_line}) ******\n[block_to_block_type(current_block]{block_to_block_type(current_block)}\n[block_to_block_type(md_line)]{block_to_block_type(md_line)}")

    ## codeblock handling
        if codefence_line and not codefence_closed:
            print(f"[B] {len(blocks)}")
            CODETEXT = not CODETEXT
            if current_block != "":
                print(f"[C] {len(blocks)}")
                blocks.append(current_block.strip())
                current_block = md_line
            else:
                print(f"[D] {len(blocks)}")
                current_block = md_line
        elif not codefence_line and codefence_closed:
            current_block = current_block + "\n" + md_line
        elif codefence_line and codefence_closed:
            print(f"[D] {len(blocks)}")
            current_block = current_block + "\n" + md_line
            blocks.append(current_block)
            current_block = ""

    ## noncodeblock handling
    # current_block empty line check
    # add line to current block
        else:
            if current_block == "":
                print(f"[E] {len(blocks)}    *line insert into empty current block")
                print(f"[E] so current_block should be empty: ({current_block})")
                current_block = md_line.strip()
                print(f"[E] after insertion current_block: ({current_block})")

    # non empty line
    # split on new line 
            else:
                print(f"is this a number? {md_line.split(". ", 1)[0]} - {int(md_line.split(". ", 1)[0])}")
                if md_line == "" or md_line == "\n":
                    blocks.append(current_block)
                    current_block = ""

# ?  if same
                if block_to_block_type(current_block) == block_to_block_type(md_line):
                    print(f"[block types are the same] {block_to_block_type(current_block)} == {block_to_block_type(md_line)}")

                # check line type
                    if line_type == BlockType.PARA:
                        print(f"[H][PARA] {len(blocks)}")
                        current_block = current_block.strip() + "\n" + md_line.strip()
                        print(f"[I][PARA] {len(blocks)}")
                    #elif line_type == BlockType.ORDE:
                    elif int(md_line.split(". ", 1)[0]):
                        current_block = current_block.strip() + "\n" + md_line.strip()
                   
                    
                    else:   #QUOT UNOR ORDE
                        print(f"[H][all the rest] {len(blocks)}")
                        #blocks.append(current_block)
                        current_block = current_block + "\n" + md_line.strip()
                        print(f"[I][all the rest] {len(blocks)}")

                        print(f"[J] {len(blocks)}")

                    print(f"[J][after line added, current_block]\n{current_block}\n\n")
    # ? if different
                if block_to_block_type(current_block) != block_to_block_type(md_line):
                    print(f"[K] {len(blocks)}")
                # else:
                # finish current block, 
                # add line to new block
                    blocks.append(current_block.strip())
                    current_block = md_line
                    print(f"[L] {len(blocks)}")
    print(f"\n[M] is anything left in current_block? \ncurrent_block: \n{current_block}\n")
    blocks.append(current_block.strip())
    print(f"[complete blocks] {blocks}\n")

    # clean blocks
    for block in blocks:
        if block.strip() != "":
            final_blocks.append(block.strip())

    print(f"[cleaned blocks] {final_blocks}\n")
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
    if match_block_headings(md_block):
        return BlockType.HEAD
    if md_block.strip().startswith("```\n") and md_block.strip().endswith("```"):
        return BlockType.CODE
    md_split = md_block.split("\n")
    QUOTESUM = 0
    UNORDEREDSUM = 0
    ORDERSUM = 0
    for line in md_split:
        if line.startswith(">"):
            QUOTESUM += 1
        if line.startswith ("- "):
            UNORDEREDSUM += 1
    if QUOTESUM == len(md_split):
        #print(f"[SANITY CHECK] QUOTESUM = {QUOTESUM}\n[SANITY CHECK] md_block = \n{md_block}\n\n")
        return BlockType.QUOT
    if UNORDEREDSUM == len(md_split):

        #print(f"[SANITY CHECK] UNORDEREDSUM = {UNORDEREDSUM}\n[SANITY CHECK] md_block = \n{md_block}\n\n")
        return BlockType.UNOR
    for n in range(1, len(md_split) + 1):
        if md_split[n-1].startswith(f"{str(n)}. "):
            ORDERSUM += 1
    if ORDERSUM == len(md_split):
        return BlockType.ORDE

    return BlockType.PARA

 
# Headings start with 1-6 # characters, followed by a space and then the heading text.
# Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
# Every line in a quote block must start with a "greater-than" character: > followed by the quote text. A space after > is allowed but not required.
# Every line in an unordered list block must start with a - character, followed by a space.
# Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
# If none of the above conditions are met, the block is a normal paragraph.
