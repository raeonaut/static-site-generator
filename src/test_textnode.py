import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("This is a another text node", TextType.BOLD)
		node3 = TextNode("This is another text node", TextType.BOLD, "https://boot.dev")
		self.assertNotEqual(node, node3)

	def test_eq_with_url(self):
		node = TextNode("This is another text node", TextType.ITALIC,"https://boot.dev")
		node3 = TextNode("This is another text node", TextType.ITALIC, "https://boot.dev")
		self.assertEqual(node, node3)


if __name__ == "__main__":
	unittest.main()