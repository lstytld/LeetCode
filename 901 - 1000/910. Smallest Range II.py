class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) <= 1:
            return 0
        A.sort()
        min_val = A[-1] - A[0]
        for i in range(len(A) - 1):
            large = max(A[i] + K, A[-1] - K)
            small = min(A[0] + K, A[i + 1] - K)
            min_val = min(min_val, large - small)
        return min_val
