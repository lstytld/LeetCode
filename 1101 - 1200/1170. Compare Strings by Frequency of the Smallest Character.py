class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(s: str) -> int:
            small_char = s[0]
            freq = 0
            for char in s:
                if char == small_char:
                    freq += 1
                if ord(char) < ord(small_char):
                    small_char = char
                    freq = 1
            return freq

        word_freq = [f(word) for word in words]
        word_freq.sort()

        ans = []
        for query in queries:
            freq = f(query)
            num = 0
            for i in range(len(words)):
                if word_freq[-1 - i] > freq:
                    num += 1
                else:
                    break
            ans.append(num)

        return ans