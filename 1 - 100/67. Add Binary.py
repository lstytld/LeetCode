class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, p = "", 0
        d = len(a) - len(b)
        a = "0" * -d + a
        b = "0" * d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            ans = str(s % 2) + ans
            p = s // 2
        return "1" + ans if p else ans
