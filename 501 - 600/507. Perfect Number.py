class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2: return False
        ans = 0
        n = 1
        while n**2 < num:
            if num%n == 0:
                ans += n + num//n
            n += 1
        return ans == num * 2


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        def perfect(n: int) -> int:
            return 2 ** (n - 1) * (2 ** n - 1)

        for n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            if num == perfect(n):
                return True
        return False