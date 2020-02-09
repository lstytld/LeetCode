# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def leaf(root: TreeNode) -> List[int]:
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]

            return leaf(root.left) + leaf(root.right)

        return leaf(root1) == leaf(root2)