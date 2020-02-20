class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        maps = [[float("inf")] * n for _ in range(n)]
        for f, t, w in edges:
            maps[f][t] = w
            maps[t][f] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        maps[j][i] = maps[i][j] = min(maps[i][k] + maps[k][j], maps[i][j])
        min_num = n
        city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if maps[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_num:
                min_num = count
                city = i
        return city
