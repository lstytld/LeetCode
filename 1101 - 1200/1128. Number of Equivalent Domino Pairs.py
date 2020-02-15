class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        if not dominoes:
            return 0
        dic = dict()
        ans = 0
        for dominoe in dominoes:
            dominoe.sort()
            dominoe = tuple(dominoe)
            if dominoe not in dic:
                dic[dominoe] = 1
            else:
                ans += dic[dominoe]
                dic[dominoe] += 1

        return ans
