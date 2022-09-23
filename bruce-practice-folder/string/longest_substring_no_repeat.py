def areDistinct(str, i, j):
 
    # Note : Default values in visited are false
    visited = [0] * (26)
 
    for k in range(i, j + 1):
        if (visited[ord(str[k]) -
                   ord('a')] == True):
            return False
             
        visited[ord(str[k]) -
                ord('a')] = True
 
    return True
 
# Returns length of the longest substring
# with all distinct characters.
def longestUniqueSubsttr(str):
     
    n = len(str)
     
    # Result
    res = 0
     
    for i in range(n):
        for j in range(i, n):
            if (areDistinct(str, i, j)):
                res = max(res, j - i + 1)
                 
    return res
