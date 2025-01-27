from textnode import *
from htmlnode import HTMLNode,LeafNode,ParentNode

test = TextNode("This is a text node", "bold", "https://www.boot.dev")
test2 = HTMLNode("h1","Title",None,{
    "href": "https://www.google.com",
    "target": "_blank",
})
leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ParentNode("p",[
        LeafNode("img", "image")
        ],)
        ],)
print(test.__repr__())
print(leaf.props_to_html())
print(node.to_html())