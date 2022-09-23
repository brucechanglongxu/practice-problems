class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
        
