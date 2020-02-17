class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        num = len(M)
        relation = [0] * (num)
        group = 0
        for i in range(num):
            if relation[i] != 0:
                continue
            group += 1
            stack = [i]
            while stack:
                p = stack.pop(0)
                relation[p] = group
                for j in range(num):
                    if M[p][j] == 1 and relation[j] == 0:
                        stack.append(j)
        return group


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        parent = [-1 for _ in range(len(M))]

        def find(parent, i):
            if parent[i] == -1: return i
            return find(parent, parent[i])

        def union(parent, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if xroot != yroot:
                parent[xroot] = yroot

        def union_find(Matrix):
            for i in range(len(Matrix)):
                for j in range(len(Matrix)):
                    if Matrix[i][j] == 1 and i != j:
                        union(parent, i, j)
            count = 0
            for i in range(len(parent)):
                if parent[i] == -1:
                    count += 1
            return count

        return union_find(M)

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        p = [[i] for i in range(n)]
        ans = n
        for i, j in itertools.combinations(range(n), 2):
            if M[i][j] == 1 and p[i] is not p[j]:
                p[i] += p[j]
                for k in p[j]:
                    p[k] = p[i]
                ans -= 1
                print(p)
        return ans
