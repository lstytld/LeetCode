class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        in_word = 0
        ans = 0
        for char in s:
            if char != " " and in_word == 0:
                ans += 1
                in_word = 1
            if char == " " and in_word == 1:
                in_word = 0
        return ans
