class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        dic = dict()
        for s in licensePlate:     
            if s.isalpha():
                s = s.lower()
                if s not in dic:
                    dic[s] = 1
                else:
                    dic[s] += 1
        ans = None
        min_len = float("inf")
        for word in words:
            if len(word) >= min_len:
                continue
            word_counter = collections.Counter(word.lower())
            for key in dic:
                if dic[key] > word_counter[key]:
                    break
            else:
                ans = word
                min_len = len(word)
        return ans
