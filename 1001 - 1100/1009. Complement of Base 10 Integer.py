class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if not N: return 1
        n = int(math.log(N)/math.log(2)) + 1
        return 2**n - 1 - N