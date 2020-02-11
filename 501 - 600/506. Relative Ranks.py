class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_new = [(num, i) for i, num in enumerate(nums)]
        nums_new.sort()
        ans = [""] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[nums_new[-1 - i][1]] = "Gold Medal"
            elif i == 1:
                ans[nums_new[-1 - i][1]] = "Silver Medal"
            elif i == 2:
                ans[nums_new[-1 - i][1]] = "Bronze Medal"
            else:
                ans[nums_new[-1 - i][1]] = str(i + 1)
        return ans

