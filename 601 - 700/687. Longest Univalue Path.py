# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        def helper(root: TreeNode):
            if not root:
                return (0, 0)

            if not root.left:
                left = (0, 0)
            else:
                left_root, left_max = helper(root.left)
                left = ((left_root + 1) * int(root.val == root.left.val), left_max)

            if not root.right:
                right = (0, 0)
            else:
                right_root, right_max = helper(root.right)
                right = ((right_root + 1) * int(root.val == root.right.val), right_max)

            return max(left[0], right[0]), max(left[0] + right[0], left[1], right[1])

        return helper(root)[1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def helper(root: TreeNode):
            if not root:
                return 0

            left_len = right_len = 0
            if root.left:
                left = helper(root.left)
                left_len = left + 1 if root.val == root.left.val else 0
            if root.right:
                right = helper(root.right)
                right_len = right + 1 if root.val == root.right.val else 0
            self.ans = max(self.ans, left_len + right_len)
            return max(left_len, right_len)

        helper(root)
        return self.ans
