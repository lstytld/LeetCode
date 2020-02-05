from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        row_num = len(M)
        col_num = len(M[0])
        res = [[0] * col_num for _ in range(row_num)]

        def smoother(row, col):
            row_min = max(row - 1, 0)
            row_max = min(row + 1, row_num - 1)
            col_min = max(col - 1, 0)
            col_max = min(col + 1, col_num - 1)
            nearby = [M[_i][_j] for _i in range(row_min, row_max + 1) for _j in range(col_min, col_max + 1)]
            return int(sum(nearby)/len(nearby))

        for i in range(row_num):
            for j in range(col_num):
                res[i][j] = smoother(i, j)

        return res
