from enum import Enum
from htmlnode import LeafNode,HTMLNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text:
            if self.text_type == other.text_type:
                if self.url == other.url:
                    return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.NORMAL :
            return LeafNode(None,self.text,None)
        elif self.text_type == TextType.BOLD :
            return LeafNode("b",self.text)
        elif self.text_type == TextType.ITALIC :
            return LeafNode("b",self.text)
        elif self.text_type == TextType.CODE :
            return LeafNode("code",self.text)
        elif self.text_type == TextType.LINK :
            return LeafNode("a",self.text,{"href" : self.url})
        elif self.text_type == TextType.IMAGE :
            return LeafNode("img","",{"src": self.url})
        else:
            raise ValueError(f"{self.text_type} is not part of the enum")
        