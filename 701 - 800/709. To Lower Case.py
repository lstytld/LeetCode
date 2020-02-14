class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for s in str:
            if 0 <= ord(s) - ord("A") < 26:
                s = chr(ord(s) - ord("A") + ord("a"))
            ans = ans + s
        return ans