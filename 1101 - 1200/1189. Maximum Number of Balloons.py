class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dic = {char: 0 for char in "balon"}
        for s in text:
            if s in dic:
                dic[s] += 1
        return min(dic["b"], dic["a"], dic["l"]//2, dic["o"]//2, dic["n"])
