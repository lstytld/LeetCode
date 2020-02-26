class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A_count = 0
        for i in range(len(s)):
            if s[i] == "A":
                A_count += 1
                if A_count > 1:
                    return False
            elif s[i-2: i+1] == "LLL":
                return False
        return True
