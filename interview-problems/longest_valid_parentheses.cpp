class Solution(object):
    def longestValidParentheses(self, s):
        m = 0
        left = 0       
        right = 0
        
        #from left to right
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            if s[i] == ')':
                right += 1                        
            if left == right:
                m = max(m, left * 2)
            elif right > left:
                left = 0
                right = 0
        
        left = 0
        right = 0
        
        #from right to left
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                left += 1
            if s[i] == ')':
                right += 1            
            if left == right:
                m = max(m, left * 2)
            elif left > right:
                left = 0
                right = 0
        return m
