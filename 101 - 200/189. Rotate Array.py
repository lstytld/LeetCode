class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        tmp = nums[len(nums) - k:]
        nums[k:] = nums[:len(nums) - k]
        nums[:k] = tmp
        return


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        count = 0
        start = 0
        while count < n:
            cur = start
            prev = nums[cur]
            while True:
                next = (cur + k) % n
                tmp = nums[next]
                nums[next] = prev
                prev = tmp
                cur = next
                count += 1
                if cur == start:
                    break
            start += 1
        return


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        nums.reverse()
        nums[:k] = nums[k - 1::-1]
        nums[k:] = nums[n - 1: k - 1:-1]




