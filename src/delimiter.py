def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes =[]
    bracket_queue = []

    for node in old_nodes:
        print(f"node: {node}")
        print(f"text_type is {text_type}")
        if text_type != node.Text_Type.TEXT:
            split_nodes += node
            print(f"text type matches - adding node to split_nodes: {split_nodes}")
        for char in range(len(node.text)):
            if node.text[char] == delimiter[0]:
                print("* detected")
                char +=1
                if len(delimiter) > 1:
                    if node.text[char] == delimiter[1]:
                        print("** detected!")
                        char += 2
                    if len(delimiter) > 2:
                        if node.text[char] == delimiter[2]:
                            print("*** detected!")
                if delimiter == bracket_queue[-1]:
                    bracket_queue.pop(-1)
                if delimiter != bracket_queue[-1]:
                    bracket_queue.append(delimiter)
