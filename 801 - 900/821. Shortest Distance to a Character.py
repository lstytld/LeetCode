class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        location = [float("-inf")]
        for i in range(len(S)):
            if S[i] == C:
                location.append(i)
        location.append(float("inf"))

        i = 1
        ans = []
        for j in range(len(S)):
            if j < location[i]:
                ans.append(min(j - location[i - 1], location[i] - j))
            elif j == location[i]:
                ans.append(0)
                i += 1
        return ans
