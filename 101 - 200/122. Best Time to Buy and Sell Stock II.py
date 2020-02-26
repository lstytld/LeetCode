class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = None
        ans = 0
        for i in range(len(prices) - 1):
            if buy is None and prices[i + 1] > prices[i]:
                buy = prices[i]
            if buy is not None and prices[i + 1] < prices[i]:
                ans += prices[i] - buy
                buy = None
        if buy is not None:
            ans += prices[-1] - buy
        return ans