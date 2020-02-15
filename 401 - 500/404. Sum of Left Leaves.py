# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, None)]
        ans = 0
        while stack:
            node, location = stack.pop()
            if node.left:
                stack.append((node.left, "left"))
            if node.right:
                stack.append((node.right, "right"))
            if not node.left and not node.right and location == "left":
                ans += node.val
        return ans
