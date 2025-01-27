from textnode import *


def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    first = None
    end = None
    for node in old_nodes :
        for i in range(0,len(node.text)):
            if node.text[i] == delimiter and first == None :
                first = i 
            if node.text[i] == delimiter and first >= 0:
                end = i 
        new_nodes.append(TextNode(node.text[:first],TextType.TEXT))
        new_nodes.append(TextNode(node.text[first + 1:end],text_type))
        new_nodes.append(TextNode(node.text[end + 1:],TextType.TEXT))
    
    if end is not None:
        print(f"Delimiter found from index {first} to {end}")
    else:
        raise ValueError("closing tag not found, invalid Markdown")
        
    return new_nodes
        