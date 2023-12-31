from binary_tree.tree_node import TreeNode
import binary_tree.traversal as traversal
from binary_tree.binary_tree import BinaryTree
import binary_tree.utils as utils

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

symmetric = btree.is_symmetric()
print(f'Is Symmetric: {symmetric}')

btree = BinaryTree.from_array([1, 2, 2, 3, 4, 4, 3])
symmetric = btree.is_symmetric()
print(f'Is Symmetric: {symmetric}')

btree = BinaryTree.from_array([5,4,8,11,None,13,4,7,2,None,None,None,1])
targetSum = 22
hasTarget = utils.has_path_sum(btree.root, targetSum)
print(f'Has target sum {targetSum}: {hasTarget}')

btree = BinaryTree.from_array([-2,None,-3])
targetSum = -5
hasTarget = utils.has_path_sum(btree.root, targetSum)
print(f'Has target sum {targetSum}: {hasTarget}')
