class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_abs = float("inf")
        ans = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_abs:
                ans.append([arr[i], arr[i + 1]])
            elif arr[i + 1] - arr[i] < min_abs:
                min_abs = arr[i + 1] - arr[i]
                ans = [[arr[i], arr[i + 1]]]
        return ans
