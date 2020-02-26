class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        num_need = dict()
        for num in A:
            if num in num_need:
                if num_need[num] == 1:
                    num_need.pop(num)
                else:
                    num_need[num] -= 1
            else:
                if num < 0:
                    if num % 2 != 0:
                        return False
                    else:
                        if num // 2 in num_need:
                            num_need[num // 2] += 1
                        else:
                            num_need[num // 2] = 1
                if num >= 0:
                    if num * 2 in num_need:
                        num_need[num * 2] += 1
                    else:
                        num_need[num * 2] = 1
        return not num_need
