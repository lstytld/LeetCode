import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for i in range(K):
            num = heapq.heappop(A)
            heapq.heappush(A, -num)
        return sum(A)
