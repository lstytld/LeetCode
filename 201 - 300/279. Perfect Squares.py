class Solution:
    def numSquares(self, n: int) -> int:

        queue = [(n, 0)]
        visited = {n}
        while queue:
            num, step = queue.pop(0)
            for i in range(1, int(num ** 0.5) + 1):
                rest = num - i ** 2
                if rest == 0: return step + 1
                if rest not in visited:
                    visited.add(rest)
                    queue.append((rest, step + 1))