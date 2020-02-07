# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return None

        min_dif = float("inf")
        if root.left:
            left = root.left
            left_dif = self.getMinimumDifference(left)
            if left_dif:
                min_dif = min(min_dif, left_dif)
            while left.right:
                left = left.right
            min_dif = min(min_dif, root.val - left.val)
        if root.right:
            right = root.right
            right_dif = self.getMinimumDifference(right)
            if right_dif:
                min_dif = min(min_dif, right_dif)
            while right.left:
                right = right.left
            min_dif = min(min_dif, right.val - root.val)
        return min_dif


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        prev_val = float("-inf")
        min_dif = float("inf")
        cur_node = root
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            cur_val = cur_node.val
            min_dif = min(min_dif, cur_val - prev_val)
            prev_val = cur_val
            cur_node = cur_node.right
        return min_dif