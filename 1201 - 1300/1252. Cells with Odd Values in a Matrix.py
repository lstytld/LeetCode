class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row_set = set()
        col_set = set()
        rows, cols = zip(*indices)
        for r in rows:
            if r not in row_set:
                row_set.add(r)
            else:
                row_set.remove(r)
        for c in cols:
            if c not in col_set:
                col_set.add(c)
            else:
                col_set.remove(c)
        return (n - len(row_set))*len(col_set) + (m - len(col_set))*len(row_set)