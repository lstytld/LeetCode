class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        n = len(nums)//2 + 1
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] = dic[num] + 1
            if dic[num] == n:
                    return num
        return None

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
