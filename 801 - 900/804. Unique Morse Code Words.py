class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = set()
        Morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        def transform(word: str) -> str:
            res = ''
            for w in word:
                res = res + Morse[ord(w) - ord("a")]
            return res

        for word in words:
            ans.add(transform(word))
        return len(ans)