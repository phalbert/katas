import unittest
from code.node_compare import compare, Node

a_node = Node(1, None, None)
b_node = Node(1, None, None)
c_node = Node(2, None, None)

d_node = Node(1, Node(1, None, None), None)
e_node = Node(1, Node(1, None, None), None)


f_node = Node(1, Node(1, None, Node(1, None, None)), None)
g_node = Node(1, Node(1, None, Node(1, None, None)), None)

class Test(unittest.TestCase):

    def test_should_return_true_for_equal_nodes(self):
        self.assertTrue(compare(a_node, b_node))
    def test_should_return_false_for_non_equal_nodes(self):
        self.assertFalse(compare(a_node, c_node))
    def test_should_handle_depth_of_one(self):
        self.assertFalse(compare(d_node, None))
    def test_should_handle_depth_of_two(self):
        self.assertTrue(compare(f_node, g_node))

if __name__ == '__main__':
    unittest.main()