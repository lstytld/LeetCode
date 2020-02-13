class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_set = set(J)
        ans = 0
        for s in S:
            if s in J_set:
                ans += 1
        return ans