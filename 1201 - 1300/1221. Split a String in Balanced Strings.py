class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) < 2:
            return 0

        num_dif = 0
        for i in range(len(s)):
            if s[i] == "R":
                num_dif += 1
            else:
                num_dif -= 1
            if num_dif == 0:
                return 1 + self.balancedStringSplit(s[i + 1::])
        else:
            return 0
