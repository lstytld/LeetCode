class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull_num = 0
        cow_num = 0
        nums = [0] * 10
        for i in range(len(secret)):
            num = int(secret[i])
            nums[num] += 1
        for i in range(len(guess)):
            num = int(guess[i])
            if nums[num] > 0:
                cow_num += 1
                nums[num] -= 1
            if guess[i] == secret[i]:
                bull_num += 1
                cow_num -= 1
        return str(bull_num) + "A" + str(cow_num) + "B"
