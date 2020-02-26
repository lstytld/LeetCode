class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        rook_row = 0
        rook_col = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_row = i
                    rook_col = j
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for r, c in dirs:
            row, col = rook_row, rook_col
            row += r
            col += c
            while 0 <= row < 8 and 0 <= col < 8:
                if board[row][col] == "p":
                    ans += 1
                    break
                elif board[row][col] == "B":
                    break
                row += r
                col += c
        return ans
