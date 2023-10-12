from binary_tree.tree_node import TreeNode
from typing import Callable, List, Optional


class BinaryTree:
    def __init__(self, root: TreeNode):
        self.root = root

    @classmethod
    def from_array(cls, values: List):
        """Accepts a list of comparable objects
           Returns a binary tree
        """
        root = TreeNode(values.pop(0))
        queue = [root]
        while values:
            left_value = values.pop(0) if values else None
            right_value = values.pop(0) if values else None
            current_node = queue.pop(0)
            if left_value:
                left = TreeNode(left_value)
                current_node.left = left
                queue.append(left)
            if right_value:
                right = TreeNode(right_value)
                current_node.right = right
                queue.append(right)
        return cls(root)

    def traverse_tree(self, traverse: Callable) -> List:
        return_list = []
        traverse(self.root, return_list)
        return return_list

    def max_depth(self) -> int:
        def answer(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            ldepth = answer(root.left)
            rdepth = answer(root.right)
            return max(ldepth, rdepth) + 1
        return answer(self.root)

    def is_symmetric(self) -> bool:
        def compare(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return compare(left.left, right.right) and compare(left.right, right.left)
        return compare(self.root.left, self.root.right)

