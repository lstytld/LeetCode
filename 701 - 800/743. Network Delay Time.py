class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))

        dist = {node: float("inf") for node in range(1, N + 1)}
        seen = [False] * (N + 1)
        dist[K] = 0

        while True:
            can_node = - 1
            can_dist = float("inf")
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < can_dist:
                    can_dist = dist[i]
                    can_node = i

            if can_node < 0:
                break
            seen[can_node] = True
            for v, time in graph[can_node]:
                dist[v] = min(dist[v], can_dist + time)

        ans = max(dist.values())
        return ans if ans < float("inf") else - 1
