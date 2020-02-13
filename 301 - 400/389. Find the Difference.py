class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        ans = 0
        for i in t:
            ans += ord(i)
        for j in s:
            ans -= ord(j)

        return chr(ans)