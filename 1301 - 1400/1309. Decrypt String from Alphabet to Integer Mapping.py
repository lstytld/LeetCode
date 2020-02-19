class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        if not s:
            return ans
        index = 1
        while index <= len(s):
            digit = s[-index]
            if digit == "#":
                index += 2
                digit = s[-index: -index + 2]
            ans = chr(ord("a") - 1 + int(digit)) + ans
            index += 1
        return ans
