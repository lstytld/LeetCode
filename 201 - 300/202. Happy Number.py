class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n not in history:
            history.add(n)
            new = 0
            while n:
                new += (n % 10) ** 2
                n = n // 10
            n = new

        if n == 1:
            return True
        return False
