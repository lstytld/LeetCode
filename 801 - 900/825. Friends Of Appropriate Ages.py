class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort(reverse=True)

        def find(start, target):
            left = start
            right = len(ages) - 1
            while left < right:
                mid = (left + right) // 2 + 1
                if ages[mid] <= target:
                    right = mid - 1
                else:
                    left = mid
            return left

        ans = 0
        older_index = - 1
        younger_index = find(0, ages[0] * 0.5 + 7)
        for i in range(len(ages)):
            if ages[i] <= 14:
                return ans
            elif i != 0 and ages[i] != ages[i - 1]:
                older_index = i - 1
                younger_index = find(younger_index, ages[i] * 0.5 + 7)
            ans += younger_index - older_index - 1
        return ans


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cage = [0 for _ in range(121)]
        for i in ages:
            cage[i] += 1

        for i in range(1, 121):
            cage[i] += cage[i - 1]

        ans = 0
        for i in range(121):
            tar = i // 2 + 7
            if tar >= i: continue
            ans += (cage[i] - cage[tar] - 1) * (cage[i] - cage[i - 1])
        return ans

