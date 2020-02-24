class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
