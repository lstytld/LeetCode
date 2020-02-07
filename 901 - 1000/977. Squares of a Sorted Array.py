class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        stack = []
        ans = []
        for num in A:
            val = num ** 2
            if num < 0:
                stack.append(val)
                continue
            if num >= 0:
                while stack and stack[-1] <= val:
                    ans.append(stack.pop())
                ans.append(val)
        while stack:
            ans.append(stack.pop())
        return ans