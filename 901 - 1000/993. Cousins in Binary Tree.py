# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return None
        stack = [root]
        next_stack = []
        values = []
        while stack:
            node = stack.pop(0)
            if node.left:
                next_stack.append(node.left)
                values.append(node.left.val)
            else:
                values.append(0)
            if node.right:
                next_stack.append(node.right)
                values.append(node.right.val)
            else:
                values.append(0)
            if not stack:
                if x in values and y in values and values.index(x) // 2 != values.index(y) // 2:
                    return True
                stack = next_stack
                next_stack = []
                values = []
        return False

class Solution(object):
    def isCousins(self, root, x, y):
        parent = {}
        depth = {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]
