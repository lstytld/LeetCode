# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parents = {}

        def dfs(node, parent=None):
            if not node:
                return
            else:
                parents[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = [(target, 0)]
        node_used = {target}
        ans = []
        while queue:
            node, dis = queue.pop(0)
            if dis == K:
                ans.append(node.val)
            if dis > K:
                break
            for next_node in [node.left, node.right, parents[node]]:
                if next_node and next_node not in node_used:
                    queue.append((next_node, dis + 1))
                    node_used.add(next_node)

        return ans

