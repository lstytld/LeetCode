class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        dif_dic = {}
        for i in range(len(nums)):
            if nums[i] not in dif_dic:
                dif_dic[nums[i]] = i
            else:
                if (i - dif_dic[nums[i]]) <= k:
                    return True
                else:
                    dif_dic[nums[i]] = i
        return False