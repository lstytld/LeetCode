class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        if not A:
            return None

        def specialcount(str1):
            res = [0] * 52
            for i, char in enumerate(str1):
                res[ord(char) - ord("a") + 26 * (i % 2)] += 1
            return tuple(res)

        ans = set()
        for str1 in A:
            ans.add(specialcount(str1))
        print(ans)
        return len(ans)

