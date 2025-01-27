import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1","Title",None,{"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1","Title",None,{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props,{"href": "https://www.google.com","target": "_blank",})

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(None,node.__repr__())

    def test_to_props(self):
        node = HTMLNode("h1","Title",None,{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_leaf(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(),"<p>This is a paragraph of text.</p>")
    
    def test_leaf_props(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_parent_recurse(self):
        node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),],)
        
        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
        
    def test_parent_children(self):
        node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ParentNode("p",[
        LeafNode("img", "image")
        ],)
        ],)
        
        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><img>image</img></p></p>')



if __name__ == "__main__":
    unittest.main()