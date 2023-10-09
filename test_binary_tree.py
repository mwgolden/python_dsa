from binary_tree.tree_node import TreeNode
from binary_tree.binary_tree import BinaryTree
import binary_tree.traversal as traversal

tree = TreeNode("F",
                TreeNode("B",
                         TreeNode("A"),
                         TreeNode("D")),
                TreeNode("G",
                            None,
                            TreeNode("I",
                                TreeNode("H"))))


btree = BinaryTree(tree)


def test_preorder_traversal():
    result = btree.traverse_tree(traversal.preorder)
    print(" ,".join(result))
    assert result == ["F", "B", "A", "D", "G", "I", "H"]


