class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) <= 2:
            return True
        groups = [-1] * len(graph)
        for i in range(len(graph)):
            if groups[i] != -1:
                continue
            group = 0
            groups[i] = group
            layer = [i]
            next_layer = []
            while layer:
                point = layer.pop(0)
                for p in graph[point]:
                    if groups[p] != -1 and groups[p] == group:
                        return False
                    if groups[p] == -1:
                        groups[p] = (group + 1) %2
                        next_layer.append(p)
                if not layer:
                    group = (group + 1)%2
                    layer = next_layer
                    next_layer = []
        return True