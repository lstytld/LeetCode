class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        dic = set()
        for char in s:
            if char not in dic:
                dic.add(char)
            else:
                dic.remove(char)
                ans += 2
        if len(dic) > 0:
            return ans + 1
        return ans