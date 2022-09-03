class Solution(object):
    """
    Class for Longest Valid Parentheses (#32)
    # https://leetcode.com/problems/longest-valid-parentheses/
    """
    def longestValidParentheses(self, s: str) -> int:
        """
        Returns the longest substring of valid well-formed parantheses
        
        Parameters
        ----------
        s : str
            string of parantheses
            
        Returns
        -------
        max_num : int
            the length of the longest valid substring of parentheses
        """
        
        max_num = 0
        left_counter = 0
        right_counter = 0
        
        # checking the string from left to right
        for i in range(len(s)):
            if s[i] == '(':
                left_counter += 1
            if s[i] == ')':
                right_counter += 1
            # when the 2 counters are equal, it's a possible valid substring
            if left_counter == right_counter:
                max_num = max(max_num, left_counter * 2)
            elif right_counter > left_counter:
                # if the number of right parentheses is greater than the left, we reset the counters
                # this means we have consecutive right parentheses without a left parenthesis in the middle, which would break the chain e.g. ())
                left_counter = 0
                right_counter = 0
        
        # we can check from the right side as well
        # resetting the counters
        left_counter = 0
        right_counter = 0
        
        # from right to left
        for i in range(len(s) - 1, -1, -1):
            # the for loop starts with the index len(s) - 1 and decreases it's value by 1 (or incrementing by -1) until i reaches -1
            if s[i] == '(':
                left_counter += 1
            if s[i] == ')':
                right_counter += 1            
            if left_counter == right_counter:
                max_num = max(max_num, left_counter * 2)
            elif left_counter > right_counter:
                # similar from how we checked the string from left to right e.g. (() is invalid while checking from the right
                left_counter = 0
                right_counter = 0
                
        return max_num
