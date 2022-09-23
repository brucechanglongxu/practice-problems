class Solution1:
    def longestValidParentheses(self, s: str) -> int:
    """
    Stack-based linear time and linear space solution to find the longest valid parentheses
    """
        stack = [-1]
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx

class Solution2:
    def longestValidParentheses(self, s: str) -> int:
    """
    Linear time and constant space solution for longest valid parentheses (increment left & right pointers)
    """
        def longestValid Parentheses(self, s: str) -> int:
            l, r = 0, 0
            mx = 0
            for p in s:
                if p == "(":
                    l+=1
                else:
                    r+= 1
                if l== r:
                    mx = max(mx, r*2)
                elif r>1:
                    l, r =0, 0
            l,r =0,0
            for p in reverse(s): 
                if p == ")":
                    r+=1
                else:
                    l+=1
                if l==r:
                    mx = max(mx,r*2)
                elif l>r:
                    l,r =0,0
            return mx
