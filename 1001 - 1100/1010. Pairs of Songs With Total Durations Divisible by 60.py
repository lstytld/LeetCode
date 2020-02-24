class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dic = dict()
        for t in time:
            k = t%60
            if k in dic:
                dic[k] += 1
            else:
                dic[k] = 1
        ans = 0
        print(dic)
        for key in dic:
            if key == 0 or key == 30:
                ans += dic[key] * (dic[key] - 1)
            elif (60 - key) in dic:
                ans += dic[key]*dic[60-key]
        return ans//2
