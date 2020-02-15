class Solution:
    def originalDigits(self, s: str) -> str:

        dic = {char: 0 for char in "eonitrhfvswuxgz"}
        for char in s:
            dic[char] += 1

        nums = [0] * 10
        nums[0] = dic["z"]
        nums[2] = dic["w"]
        nums[4] = dic["u"]
        nums[6] = dic["x"]
        nums[8] = dic["g"]
        nums[5] = dic["f"] - nums[4]
        nums[7] = dic["v"] - nums[5]
        nums[3] = dic["h"] - nums[8]
        nums[9] = dic["i"] - nums[5] - nums[6] - nums[8]
        nums[1] = dic["o"] - nums[0] - nums[2] - nums[4]

        ans = ""
        for i, n in enumerate(nums):
            ans = ans + str(i) * n
        return ans
