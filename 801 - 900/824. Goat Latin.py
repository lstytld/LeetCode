class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split(" ")
        ans = 0
        for i in range(len(S)):
            word = S[i]
            if word[0].lower() in ["a", "e", "i", "o", "u"]:
                word = word + "ma" + "a" * (i + 1)
            else:
                word = word[1:] + word[0] + "ma" + "a" * (i + 1)
            if not ans:
                ans = word
            else:
                ans = ans + " " + word
        return ans