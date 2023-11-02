from typing import Optional
from binary_tree.tree_node import TreeNode


def count_univalue_subtrees(root: Optional[TreeNode]) -> int:
    count = 0

    def dfs(node: Optional[TreeNode]) -> bool:
        nonlocal count
        if node is None:
            return True
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False
            count += 1
            return True
        return False

    dfs(root)
    return count


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
