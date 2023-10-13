from typing import Optional
from binary_tree.tree_node import TreeNode


def has_path_sum(root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False
    targetSum -= root.val
    if is_leaf_node(root):
        return targetSum == 0
    return has_path_sum(root.left, targetSum) or has_path_sum(root.right, targetSum)


def is_leaf_node(root: TreeNode) -> bool:
    if root.left or root.right:
        return False
    return True
