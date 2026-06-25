def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes =[]
    bracket_queue = []


    for node in old_nodes:
        print(f"node: {node}")
        print(f"text_type is {text_type}")
        if text_type != "plain text":
            split_nodes.append(node)
        
        for char in range(len(node.text)):
            d_len = len(delimiter)
            local_d = ""
            for d in range(0, d_len):
                if node.text[char] == delimiter[d]:
                    local_d += node.text[char]
                    char +=1
            if delimiter in local_d:
                if delimiter in bracket_queue[::-1]:
                    bracket_queue.pop(-1)
                elif delimiter != bracket_queue[::-1]:
                    bracket_queue.append(delimiter)
                    split_nodes += node.text.split(local_d, 2)
                else:
                    print("wasnt expecting this")
                

        print(" \n ******************************* \n ")
        return split_nodes
