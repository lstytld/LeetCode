class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves:
            return True
        dic = collections.Counter(moves)
        for i in "LURD":
            if i not in dic:
                dic[i] = 0
        if dic["L"] == dic["R"] and dic["U"] == dic["D"]:
            return True
        return False