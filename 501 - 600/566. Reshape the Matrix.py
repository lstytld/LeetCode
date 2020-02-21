class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums
        ans = []
        for i in range(r):
            ans.append([])
            for j in range(c):
                t = i * c + j
                ans[i].append(nums[t//col][t%col])
        return ans
