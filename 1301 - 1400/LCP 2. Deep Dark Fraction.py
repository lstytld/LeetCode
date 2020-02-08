class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if not cont: return None
        if len(cont) == 1: return [cont[0], 1]

        a_0 = cont[0]
        m, n = self.fraction(cont[1:])

        n = a_0 * m + n
        m = m // math.gcd(m, n)
        n = n // math.gcd(m, n)
        return [n, m]
