from binary_tree.tree_node import TreeNode
import binary_tree.traversal as traversal
from binary_tree.binary_tree import BinaryTree

#btree = BinaryTree.from_array([1, None, 2, 3])
btree = BinaryTree.from_array([1, 2, None, None, 3, 4, 5])
preorder = btree.traverse_tree(traversal.preorder)
print(', '.join(str(n) for n in preorder))

itpreorder = btree.traverse_tree(traversal.iterative_preorder)
print(', '.join(str(n) for n in itpreorder))


mpreorder = btree.traverse_tree(traversal.morris_preorder)
print(', '.join(str(n) for n in mpreorder))

levelorder = btree.traverse_tree(traversal.levelorder)
print(', '.join(str(n) for n in levelorder))

maxdepth = btree.max_depth()
print(f'Max Depth: {maxdepth}')