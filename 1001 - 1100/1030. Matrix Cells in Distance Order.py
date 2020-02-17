class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        max_dis = max(r0, R - r0 - 1) + max(c0, C - c0 - 1)
        dis_list = [[] for i in range(max_dis + 1)]
        for r in range(R):
            for c in range(C):
                dis = abs(r - r0) + abs(c - c0)
                dis_list[dis].append([r, c])
        ans = []
        for l in dis_list:
            ans.extend(l)
        return ans
