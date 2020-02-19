class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_need = dict()
        for i in range(len(nums)):
            if nums[i] in num_need:
                return [num_need[nums[i]], i]
            else:
                num_need[target - nums[i]] = i
