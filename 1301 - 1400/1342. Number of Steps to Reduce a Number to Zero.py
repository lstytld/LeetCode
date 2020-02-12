class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num > 0:
            ans += num % 2 + 1
            num = num // 2
        return ans - 1