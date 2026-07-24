import re   

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def match_block_headings(block):
    matches = re.findall(r"(^\#{1,6} (\w))", block)
    print(f"[block headings match in progress] {matches}")
    if matches:
        return True

def match_block_multiline_code(block):
    # this might be better done with .startswith() and .endswith()
    pass

def match_block_quote(block):
    # this one just needs a .sartswith()    
    pass

def match_block_unordered_list(block):
    pass

def match_block_ordered_list(block):
    # need recursion as well as regex
    pass




# Headings start with 1-6 # characters, followed by a space and then the heading text.
# Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
# Every line in a quote block must start with a "greater-than" character: > followed by the quote text. A space after > is allowed but not required.
# Every line in an unordered list block must start with a - character, followed by a space.
# Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
# If none of the above conditions are met, the block is a normal paragraph.
