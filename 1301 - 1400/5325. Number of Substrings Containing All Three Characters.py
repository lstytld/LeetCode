class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_index = {"a": -1, "b": -1, "c": -1}
        ans = 0
        for i in range(len(s)):
            last_index[s[i]] = i
            ans += min(last_index["a"], last_index["b"], last_index["c"]) + 1
        return ans


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        myc = {"a": 0, "b": 0, "c": 0}
        left = 0
        for right in range(len(s)):
            myc[s[right]] += 1
            while myc["a"] and myc["b"] and myc["c"]:
                ans += len(s) - right
                myc[s[left]] -= 1
                left += 1
        return ans
