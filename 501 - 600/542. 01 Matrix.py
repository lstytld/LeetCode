class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        ans = [[float("inf")] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                    continue
                left = ans[i][j - 1] if j > 0 else float("inf")
                upper = ans[i - 1][j] if i > 0 else float("inf")
                ans[i][j] = min(left + 1, upper + 1, ans[i][j])

        for i in range(row):
            for j in range(col):
                if matrix[row - 1 - i][col - 1 - j] == 0:
                    ans[row - 1 - i][col - 1 - j] = 0
                    continue
                right = ans[row - 1 - i][col - j] if j > 0 else float("inf")
                lower = ans[row - i][col - 1 - j] if i > 0 else float("inf")
                ans[row - 1 - i][col - 1 - j] = min(right + 1, lower + 1, ans[row - 1 - i][col - 1 - j])
        return ans
