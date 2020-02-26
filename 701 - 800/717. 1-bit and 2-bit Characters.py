class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits or bits[-1] == 1:
            return False
        index = 0
        while index < len(bits) - 1:
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        if index == len(bits):
            return False
        return True
