"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        if not root.children:
            return [root.val]

        ans = []
        for child in root.children:
            ans = ans + self.postorder(child)
        ans = ans + [root.val]
        return ans


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None

        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.children:
                for child in node.children:
                    stack.append(child)

        return ans[::-1]




