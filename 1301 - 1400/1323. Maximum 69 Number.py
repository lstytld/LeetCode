class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        n = len(s)
        for i in range(n):
            if s[i] =="6":
                return num + 3 * 10 ** (n - i -1)
        else:
            return num