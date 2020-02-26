class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
               "IV": 3, "IX": 8, "XL": 30, "XC": 80, "CD": 300, "CM": 800}
        ans = 0
        for i in range(len(s)):
            val = dic.get(s[i - 1:i + 1], dic[s[i]])
            ans += val
        return ans