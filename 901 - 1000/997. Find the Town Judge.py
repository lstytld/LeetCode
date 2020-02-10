class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_dict = [[0, 0] for _ in range(1, N + 1)]
        for t in trust:
            trust_dict[t[0] - 1][0] += 1
            trust_dict[t[1] - 1][1] += 1
        for p in range(1, N + 1):
            if trust_dict[p - 1][0] == 0 and trust_dict[p - 1][1] == N - 1:
                return p
        return -1
