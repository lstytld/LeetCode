class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        n = int(area ** 0.5)
        while area % n != 0:
            n -= 1
        return [area//n, n]
