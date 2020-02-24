class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        num_dif = (a | b) ^ c
        num_11 = a & b & ~c

        def num_one(num):
            ans = 0
            while num:
                num = num & (num - 1)
                ans += 1
            return ans

        return num_one(num_dif) + num_one(num_11)
