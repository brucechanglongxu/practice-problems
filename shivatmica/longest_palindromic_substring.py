class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        def isPalindrome(s, j, k):
            if (j == k):
                return True
            elif (k - j == 1) and (s[j] == s[k]):
                return True
            else:
                if (j <= k):
                    if s[i: j +1] not in palindromes:
                        return isPalindrome(s, j + 1, k - 1) and (s[j] == s[k])
        longestPalindrome = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if (j - i + 1 > len(longestPalindrome)):
                    if s[i: j +1] not in palindromes:
                        if (isPalindrome(s, i, j)):
                            longestPalindrome = s[i: j+1]
                            if len(longestPalindrome) > 1: 
                                palindromes.append(longestPalindrome)
        return longestPalindrome
