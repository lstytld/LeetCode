class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modify_num = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modify_num == 1:
                    return False
                else:
                    if (i == 1 or nums[i - 2] <= nums[i]) or (i == len(nums) - 1 or nums[i - 1] <= nums[i + 1]):
                        modify_num += 1
                    else:
                        return False
        return True
