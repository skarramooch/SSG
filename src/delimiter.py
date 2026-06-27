from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    print(" \n **************START***************** \n ")
    split_nodes =[]
    bracket_queue = []


    for node in old_nodes:
        #print(f"node: {node}")
        #print(f"text_type is {text_type}")
        # return original node if not plain text
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            print(f"you should only see this if node.text_type!= TextType.TEXT : {node.text_type}")
        
        # search for delimiter
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
                    split_nodes.append(node.text.split(local_d))
                else:
                    raise Exception("wasnt expecting this, delimiter should be in bracket queue or not!")
        #print(split_nodes) 

        #print("now defining nodes")
        #print(f"can we slice plit_nodes? split_nodes[0] is {split_nodes[0]}")
        #print(f"len(split_nodes)>1 ({len(split_nodes)})") 
        #if len(split_nodes) > 1:
            #print(f"len(split_nodes[1] == 2 ({len(split_nodes[1])})")
        

        #if len(split_nodes) > 1 and len(split_nodes[1]) == 2:
        #    first_frag = split_nodes[1][0]
        #    second_frag = split_nodes[1][1]
        #    #print(f"first frag '{first_frag}', second frag '{second_frag}'")
        #    split_nodes = [TextNode({first_frag}, TextType.TEXT),
        #                   TextNode({second_frag}, text_type)]
        #if len(split_nodes) > 1 and len(split_nodes[1]) == 3:
        #    first_frag = split_nodes[1][0]
        #    second_frag = split_nodes[1][1]
        #    third_frag = split_nodes[1][2]
        #    #print(f"first frag '{first_frag}', second frag '{second_frag}', third frag '{third_frag}'")
        #    split_nodes = [TextNode({first_frag}, TextType.TEXT),
        #                   TextNode({second_frag}, text_type),
        #                   TextNode({third_frag}, TextType.TEXT)]
        #else:
        #    print("more than one delimiter set has been used - need to revisit delimiter.py")

        # redoing the frags
        new_nodes = []
        for node in split_nodes:
            for frag in node:
                print(f"frag '{frag}'")
                new_nodes.append(TextNode(frag, TextType.TEXT))





        print(f"returning new nodes:\n{new_nodes}")
        print(f"after checking len(local_d): {len(local_d)}: {local_d}")
        #if len(local_d) > 0:
        #   } raise Exception("unmatched delimeters found Invalid Markdown Syntax")

        print(" \n **************FINISH***************** \n ")
        return new_nodes
