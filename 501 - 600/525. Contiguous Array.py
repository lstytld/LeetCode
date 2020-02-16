class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        s = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                s += 1
            else:
                s -= 1
            if s not in dic:
                dic[s] = i
            else:
                max_len = max(max_len, i - dic[s])
        return max_len
