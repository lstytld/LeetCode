class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if not matrix:
            return ans
        n = len(matrix)
        m = len(matrix[0])
        i = j = 0
        if not matrix:
            return ans
        while i + j < m + n - 1:
            ans.append(matrix[i][j])
            if (i + j) % 2 == 0:
                if j == m - 1:
                    i += 1
                    continue
                if i == 0:
                    j += 1
                    continue
                i -= 1
                j += 1
            if (i + j) % 2 == 1:
                if i == n - 1:
                    j += 1
                    continue
                if j == 0:
                    i += 1
                    continue
                i += 1
                j -= 1
        return ans


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n, r = len(matrix), len(matrix) and len(matrix[0]), []
        for l in range(m + n - 1):
            temp = [matrix[i][l - i] for i in range(max(0, l + 1 - n), min(l + 1, m))]
            r += temp if l % 2 else temp[::-1]
        return r
