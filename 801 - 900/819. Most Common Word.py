class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban_set = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        count = collections.Counter(paragraph.lower().split())

        ans, best = "", 0
        for word in count:
            if count[word] > best and word not in ban_set:
                ans, best = word, count[word]
        return ans


