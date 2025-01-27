import unittest

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


if __name__ == "__main__":
    unittest.main()