import unittest
from delimiter import split_nodes_delimiter
from enum import Enum
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test__repr(self):
        test = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(test.__repr__(),"TextNode(This is a text node,bold,https://www.boot.dev)")

    def test_eqa(self):
        test = TextNode("This is a text node", "bold", "https://www.boot.dev")
        test2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(test.__eq__(test2),True)
    def text_to_html(self):
        test = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        self.assertEqual(test.text_node_to_html_node(),'<a href="https://www.google.com">This is a link</a>')
    
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
])

if __name__ == "__main__":
    unittest.main()