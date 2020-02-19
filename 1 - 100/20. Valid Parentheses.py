class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char not in dic:
                stack.append(char)
            else:
                if not stack or stack.pop() != dic[char]:
                    return False
        return True if not stack else False