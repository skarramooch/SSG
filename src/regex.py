import re   

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    #print(f"[my images match] {matches}")
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    #print(f"[my links match] {matches}")
    return matches

def boot_sample_images(text):
    boot_image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return boot_image_matches

def boot_sample_links(text):
    boot_link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return boot_link_matches
