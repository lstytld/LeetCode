class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0, 0]
        for i in range(2, len(cost) + 1):
            ans.append(min(ans[-1] + cost[i-1], ans[-2] + cost[i-2]))
        return ans[-1]