class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        ans = []
        for index, value in enumerate(nums):
            if len(ans) < 2:
                heapq.heappush(ans, (value, index))
                continue
            if value > ans[0][0]:
                heapq.heapreplace(ans, (value, index))

        max_small = heapq.heappop(ans)
        max_large = heapq.heappop(ans)
        return max_large[1] if max_large[0] >= 2 * max_small[0] else -1