class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_v = min(nums)
        return sum(num - min_v for num in nums)

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        if not nums:
            return ans
        min_v = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min_v:
                ans += i *(min_v - nums[i])
                min_v = nums[i]
            else:
                ans += nums[i] - min_v
        return ans
