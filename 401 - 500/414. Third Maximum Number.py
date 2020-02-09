class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        heap = [float("-inf")] * 3
        heapq.heapify(heap)
        for num in nums:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
