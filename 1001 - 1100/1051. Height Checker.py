class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        ans = 0
        for i in range(len(a)):
            if a[i] != heights[i]:
                ans += 1
        return ans


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h_list = [0] * 101
        for h in heights:
            h_list[h] += 1
        ans = 0
        j = 0
        for i in range(1, 101):
            for _ in range(h_list[i]):
                if heights[j] != i:
                    ans += 1
                j += 1
        return ans
