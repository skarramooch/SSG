def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes =[]
    bracket_queue = []

    for node in old_nodes:
        if text_type != TextType.TEXT:
            split_nodes += old_nodes
        for char in range(len(node)):
            if node[char] == "*":
                if node{char+1] =="*":
                    print("** detected!")
                    char += 2
            if node[char] == "_":
                print("_ detected!")
                char += 1
