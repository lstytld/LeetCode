class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for s in S:
            if s == "(":
                stack.append(0)
            else:
                val = stack.pop()
                if val == 0:
                    stack.append(stack.pop() + 1)
                else:
                    stack.append(stack.pop() + val * 2)
        return stack.pop()


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = 0
        depth = 0
        for i in range(len(S)):
            if S[i] == "(":
                depth += 1
            else:
                depth -= 1
                if S[i - 1] == "(":
                    ans += 2 ** depth
        return ans
