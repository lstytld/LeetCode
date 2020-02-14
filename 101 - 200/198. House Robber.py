class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = 0
        cur = nums[0]
        for i in range(1, len(nums)):
            prev1, prev2, cur = prev2, cur, max(cur, prev2 + nums[i])
        return cur
