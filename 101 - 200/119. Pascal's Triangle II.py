class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for row in range(1, rowIndex + 1):
            ans.insert(0,1)
            for i in range(1, row):
                ans[i] = ans[i] + ans[i+1]
        return ans