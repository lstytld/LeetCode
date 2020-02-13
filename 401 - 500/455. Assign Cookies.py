class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        s.sort()
        while g and s:
            child = g.pop()
            if child <= s[-1]:
                s.pop()
                ans += 1
        return ans
