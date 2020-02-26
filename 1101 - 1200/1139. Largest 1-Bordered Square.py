class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        nums = [[[0, 0] for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(row):
            for j in range(col):
                nums[i + 1][j + 1][0] = nums[i + 1][j][0] + 1 if grid[i][j] else 0
                nums[i + 1][j + 1][1] = nums[i][j + 1][1] + 1 if grid[i][j] else 0

        def check(row, col, l):
            if nums[row + l][col + l][0] >= l and nums[row + l][col + l][1] >= l and nums[row + l][col + 1][1] >= l and \
                    nums[row + 1][col + l][0] >= l:
                return True
            else:
                return False

        l = min(row, col)
        while l > 0:
            for i in range(row - l + 1):
                for j in range(col - l + 1):
                    if check(i, j, l):
                        return l ** 2
            l -= 1
        return 0
