class Solution(object):
    """
    Class for Wildcard Matching (#44)
    # https://leetcode.com/problems/wildcard-matching/
    """
    def isMatch(self, s: str, p: str) -> bool:
        """
        Returns whether the sequence (s) matches the pattern (p)
            
        Parameters
        ----------
        s : str
            The inputted string
        p : str
            The inputted pattern with which we must check if it matches the string (s)
            
        Returns
        -------
        dp_table[-1][-1] : bool
            The boolean value (True/False) part of the DP table, representing whether the wildcard pattern matches the string
        """
        
        # we take the respective lengths of s and p and add 1
        # the dp_table will range from 0 to length(s) + 1 and 0 to length(p) + 1 where the first index refers to the empty string 
        # the index i corresponds to the ith character in the string
        a = len(s) + 1
        b = len(p) + 1
        
        # creates a multi_dimensional array to confirm the matches of different indices
        dp_table = [[False] * b for _ in range(a)]
        
        # when both s and p are empty strings, they will still match
        dp_table[0][0] = True 
        
        # where s is the empty string, patterns with at least 1 "*" matches everything
        for i in range(1, b):
            if p[i - 1] != '*':
                break
            # we set the matches true until we get to the first character that isn't "*"
            dp_table[0][i] = True
            
        # for any case with an empty pattern (possible according to the question) we don't need to change anything
        # an empty pattern doesn't match any string so the default False remains False
 
        # we iterate through the table and each dp_table[j][k] depends on its previous neighbors
        # dp_table's bool values are recursive and depend on the previous inputted values
        for j in range(1, a):
            for k in range(1, b):
                if p[k-1] == '*':
                    # if the character is "*", that position in the dp_table is True as long as one of the previous consecutive bools are True
                    # "*" matches any character so we don't need to check its match with the string's letters
                    dp_table[j][k] = dp_table[j - 1][k] or dp_table[j][k - 1]
                elif s[j - 1] == p[k - 1] or p[k - 1] == '?':
                    # we just continue what it formerly was if the next letter also matches/ is acceptable 
                    # if it was True for the dp_table[j - 1][k - 1] entry and the next letter matches, we continue for it to be True
                    # if it was formerly False, even if the next letter is acceptable, the bool doesn't change and remains False (the default value)
                    dp_table[j][k] = dp_table[j - 1][k - 1]
                    
        # we return the last value in the array since it depends on the values from the rest of the array
        # it's the last element along the diagonal of the array
        return dp_table[-1][-1]
