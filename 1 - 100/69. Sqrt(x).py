class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x
        while lower <= upper:
            m = (lower + upper) // 2
            if m ** 2 == x:
                return m
            elif m ** 2 > x:
                upper = m - 1
            else:
                lower = m + 1
        return upper
