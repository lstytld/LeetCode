# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        if not root:
            return []

        stack = [root]
        new_stack = []
        values = []
        ans = []
        while stack:
            node = stack.pop(0)
            values.append(node.val)
            if node.left:
                new_stack.append(node.left)
            if node.right:
                new_stack.append(node.right)
            if not stack:
                ans.append(sum(values) / len(values))
                values = []
                stack = new_stack
                new_stack = []
        return ans
