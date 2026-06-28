from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    print(" \n **************START***************** \n ")
    split_nodes =[]
    bracket_queue = []

    d_len = len(delimiter)

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            print(f"you should only see this if node.text_type!= TextType.TEXT : {node.text_type}")
        
        # search for delimiter
        for char in range(len(node.text)):
            local_d = ""
            for d in range(0, d_len):
                # print(f"[delimiter] for loop, for d: {d}, node.text[char]: {node.text[char]}, local_d: {local_d}")
                if node.text[char] == delimiter[d]:
                    DSEARCH = True
                    #print(f"[delimiter] char ({node.text[char]}) matches delimiter[d] ({delimiter[d]}), DSEARCH is {DSEARCH} ")
                    local_d += node.text[char]
                    char +=1
                    #print(f"[delimiter] char increased to {char}, local_d: {local_d}")

                
            if delimiter in local_d:
                if delimiter in bracket_queue[::-1]:
                    bracket_queue.pop(-1)
                    print(f"removed delimiter from local_d, local_d: {local_d}")
                elif delimiter != bracket_queue[::-1]:
                    bracket_queue.append(delimiter)
                    print(f"added delimitor to local_d, local_d: {local_d}")
                    split_nodes.append(node.text.split(local_d))
                else:
                    raise Exception("wasnt expecting this, delimiter should be in bracket queue or not!")

        # redoing the frags
        new_nodes = []
        for node in split_nodes:
            for frag in range(0, len(node)):
                if frag % 2 == 0:
                    new_nodes.append(TextNode(node[frag], TextType.TEXT))
                if frag % 2 == 1:
                    new_nodes.append(TextNode(node[frag], text_type))






        # print(f"returning new nodes:\n{new_nodes}")
        print(f"after checking len(local_d): {len(local_d)}: {local_d}")
        #if len(local_d) > 0:
        #   } raise Exception("unmatched delimeters found Invalid Markdown Syntax")

        print(" \n **************FINISH***************** \n ")
        return new_nodes
