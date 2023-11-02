import unittest
from binary_tree.binary_tree import BinaryTree
from binary_tree.utils import count_univalue_subtrees


class TestBinaryTreeMethods(unittest.TestCase):
    def test_count_univalue_subtrees(self):
        t = [5, 1, 5, 5, 5, None, 5]
        tree = BinaryTree.from_array(t)
        count = count_univalue_subtrees(tree.root)
        self.assertEqual(count, 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
