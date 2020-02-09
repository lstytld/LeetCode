class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total_sum = sum(range(1, len(nums) + 1))
        set_sum = sum(set(nums))
        return [sum(nums) - set_sum, total_sum - set_sum]


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor, xor1, xor2 = 0, 0, 0
        for i in range(1, len(nums) + 1):
            xor = xor ^ i
        for num in nums:
            xor = xor ^ num
        right = xor & ~ (xor - 1)

        for num in nums:
            if (num & right) != 0:
                xor1 = xor1 ^ num
            else:
                xor2 = xor2 ^ num

        for i in range(1, len(nums) + 1):
            if (i & right) != 0:
                xor1 = xor1 ^ i
            else:
                xor2 = xor2 ^ i

        for num in nums:
            if num == xor1:
                return [xor1, xor2]
        return [xor2, xor1]