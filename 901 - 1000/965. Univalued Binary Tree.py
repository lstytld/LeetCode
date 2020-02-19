# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True

        val = root.val
        if root.left:
            if root.left.val != val or not self.isUnivalTree(root.left):
                return False
        if root.right:
            if root.right.val != val or not self.isUnivalTree(root.right):
                return False
        return True
