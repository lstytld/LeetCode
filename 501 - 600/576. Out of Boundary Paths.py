class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        board = [[0] * n for _ in range(m)]
        board[i][j] = 1
        ans = 0
        for t in range(N):
            board_tmp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for next_r, next_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        row = r + next_r
                        col = c + next_c
                        if 0 <= row < m and 0 <= col < n:
                            board_tmp[row][col] += board[r][c]
                        else:
                            ans += board[r][c]
            board = board_tmp
        return ans % (10 ** 9 + 7)
