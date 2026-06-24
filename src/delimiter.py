def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes =[]
    bracket_queue = []

    for node in old_nodes:
        print(f"node: {node}")
        print(f"text_type is {text_type}")
        if text_type != "plain text":
            split_nodes.append(node)
            #print(f"text type not plain text - adding node UNALTERED to split_nodes: {split_nodes}")
        for char in range(len(node.text)):
            if node.text[char] == delimiter[0]:
                print(f"{delimiter[0]} detected {node}")
                char +=1
                if len(delimiter) > 1:
                    if node.text[char] == delimiter[1]:
                        print(f"{delimiter[0:1]} detected! {node}")
                        char += 2
                    if len(delimiter) > 2:
                        if node.text[char] == delimiter[2]:
                            print(f"{delimiter[0:2]} detected! {node}")
                if delimiter == bracket_queue[::-1]:
                    print(f"bracket_queue[::-1]: {bracket_queue[::-1]}")
                    print(f"bracket_queue before removing is {bracket_queue}")
                    bracket_queue.pop(-1)
                    print(f"bracket_queue after removing is {bracket_queue}")

                if delimiter != bracket_queue[::-1]:
                    print(f"bracket_queue[::-1]: {bracket_queue[::-1]}")
                    print(f"bracket_queue before appending is {bracket_queue}")
                    bracket_queue.append(delimiter)
                    print(f"bracket_queue after appending is {bracket_queue}")
        print(" \n ******************************* \n ")
        return split_nodes
