# https://leetcode.com/problems/longest-valid-parentheses/
def longest_valid_parentheses(s: str = "(()") -> int:
    """
    Finds and returns the length of the longest well-formed parentheses substring in s

    :param s: String containing just '(' and ')'
    :return: length of the longest well-formed parentheses substring in s
    """
    # holds the length of the longest well-formed parentheses substring in s
    longest = 0
    # stack is initialized with -1 to make idx - stack[-1] accurate in certain cases
    stack = [-1]
    for idx in range(len(s)):
        if s[idx] == "(":
            stack.append(idx)
        elif stack:
            stack.pop()
            if stack:
                # idx - stack[-1] finds the length of the substring between the current idx and the one at top of the stack
                longest = max(longest, idx - stack[-1])
            else:
                # appending the current idx makes idx - stack[-1] accurate in certain cases
                stack.append(idx)

    return longest
