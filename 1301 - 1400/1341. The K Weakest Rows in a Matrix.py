class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i, row in enumerate(mat):
            num = 0
            for j in row:
                if j == 0:
                    break
                num += 1
            if len(heap) < k:
                heapq.heappush(heap, (-num, -i))
            elif heap[0] < (-num, -i):
                heapq.heapreplace(heap, (-num, -i))

        ans = []
        for i in range(k):
            t = heapq.heappop(heap)
            ans.insert(0, -t[1])
        return ans
