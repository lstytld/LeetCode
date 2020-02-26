class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        min_neg = len(grid[0])
        for i in range(len(grid)):
            if min_neg == 0:
                break
            for j in range(len(grid[0])):
                if j == min_neg:
                    break
                if grid[i][j] < 0:
                    ans += (min_neg - j) * (len(grid) - i)
                    min_neg = j
                    break
        return ans


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        min_neg = len(grid[0])
        for i in range(len(grid)):
            if min_neg == 0:
                break
            j = min_neg - 1
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            ans += (min_neg - j - 1) * (len(grid) - i)
            min_neg = j + 1
        return ans
