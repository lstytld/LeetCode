class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for r in range(row):
            for c in range(col):
                num = grid[r][c]
                ans += 6 * num - 2 * max(num - 1, 0)
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r_new = r + i
                    c_new = c + j
                    if 0 <= r_new < row and 0 <= c_new < col:
                        ans -= min(num, grid[r_new][c_new])
        return ans
