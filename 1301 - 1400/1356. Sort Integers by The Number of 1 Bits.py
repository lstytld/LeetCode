class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        def digit(num):
            if num == 0:
                return 0
            return 1 + digit(num & (num - 1))

        return sorted(arr, key=lambda x: (digit(x), x))
