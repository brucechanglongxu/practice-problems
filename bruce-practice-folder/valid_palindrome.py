# A phrase is a palindrome if after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Given a string s, return true if it is a palindrome, or false otherwise. 

# Maintain two pointers (left and right)
def isPalindrome(s):
  left = 0
  right = len(s) - 1
  while left < right:
    while left < right and not s[left].isalnum():
      left += 1
    while left < right and not s[right].isalnum():
      right -= 1
    if s[left].lower() != s[right].lower():
      return False
    else:
      left += 1
      right -= 1
  return True      
