class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        upper_area = 0
        row_area = [0] * row
        col_area = [0] * col
        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    upper_area += 1
                if grid[i][j] > row_area[i]:
                    row_area[i] = grid[i][j]
                if grid[i][j] > col_area[j]:
                    col_area[j] = grid[i][j]
        return upper_area + sum(row_area) + sum(col_area)
