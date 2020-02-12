class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if "" in strs:
            return ""

        pre = strs[0][0:1]
        for s in strs:
            if s[0:1] != pre:
                return ""
        else:
            return pre + self.longestCommonPrefix([s[1:] for s in strs])
