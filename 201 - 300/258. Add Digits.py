class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        newnum = 0
        while num != 0:
            newnum += num % 10
            num = num // 10
            if num == 0:
                if newnum < 10:
                    return newnum
                num = newnum
                newnum = 0