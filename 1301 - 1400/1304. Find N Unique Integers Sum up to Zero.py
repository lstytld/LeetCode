class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n):
            ans[0] -= i
            ans.append(i)
        return ans