from binary_tree.tree_node import TreeNode
from typing import List, Optional


def preorder(node: TreeNode, return_list: List) -> list | None:
    if node is None:
        return
    return_list.append(node.val)
    preorder(node.left, return_list)
    preorder(node.right, return_list)

    return return_list


def inorder(node: TreeNode, return_list: List) -> list | None:
    if node is None:
        return
    inorder(node.left, return_list)
    return_list.append(node.val)
    inorder(node.right, return_list)

    return return_list


def postorder(node: TreeNode, return_list: List) -> List | None:
    if node is None:
        return
    postorder(node.left, return_list)
    postorder(node.right, return_list)
    return_list.append(node.val)

    return return_list


def levelorder(root: Optional[TreeNode], return_list: List) -> List[List]:
    if root is None:
        return []
    queue = [root]
    while queue:
        size = len(queue)
        level = []
        for i in range(0, size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return_list.append(level)

    return return_list


def iterative_preorder(root: TreeNode, return_list) -> List:
    stack = [root]
    while stack:
        current_node = stack.pop()
        if current_node:
            return_list.append(current_node.val)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

    return return_list


def morris_preorder(root: TreeNode, return_list: List) -> List:
    current_node = root
    while current_node:
        # if there is no left child, go for the right child
        # otherwise, find the last node in the left subtree
        if not current_node.left:
            return_list.append(current_node.val)
            current_node = current_node.right
        else:
            last_node = current_node.left
            while last_node.right and last_node.right != current_node:
                last_node = last_node.right

            # if the last_node is not modified, we let
            # current_node be its right child. Otherwise,
            # it means we have finished the entire left subtree
            if not last_node.right:
                return_list.append(current_node.val)
                last_node.right = current_node
                current_node = current_node.left
            else:
                last_node.right = None
                current_node = current_node.right

    return return_list

