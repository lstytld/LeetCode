class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startcolor = image[sr][sc]
        if startcolor == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            row, col = stack.pop()
            image[row][col] = newColor
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                row_new = row + i
                col_new = col + j
                if 0 <= row_new < len(image) and 0 <= col_new < len(image[0]) and image[row_new][col_new] == startcolor:
                    stack.append((row_new, col_new))
        return image

