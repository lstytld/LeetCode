class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        first = 0
        second = 1
        third = 1
        for i in range(n - 2):
            new = first + second + third
            first, second, third = second, third, new
        return third