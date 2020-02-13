# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def helper(root):
            if not root:
                return 0

            left_len = right_len = 0
            if root.left:
                left_len = helper(root.left) + 1
            if root.right:
                right_len = helper(root.right) + 1
            self.ans = max(self.ans, left_len + right_len)
            return max(left_len, right_len)

        helper(root)
        return self.ans

