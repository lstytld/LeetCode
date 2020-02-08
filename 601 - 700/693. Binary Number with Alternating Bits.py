class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        str1 = bin(n)[2::]
        for i in range(len(str1) - 1):
            if str1[i] == str1[i + 1]:
                return False
        return True

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return ('00' not in bin(n)) and ('11' not in bin(n))
