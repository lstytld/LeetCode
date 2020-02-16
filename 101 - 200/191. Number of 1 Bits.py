class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n-1)
            ans += 1
        return ans

class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2::]
        ans = 0
        for c in b:
            if c == "1":
                ans += 1
        return ans
