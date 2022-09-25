# https://leetcode.com/problems/longest-valid-parentheses/
def longest_valid_parentheses(s: str = "(()") -> int:
    """
    Finds and returns the length of the longest well-formed parentheses substring in s
    Algorithm: A stack is used to store the indices of the parentheses. When an open parenthesis is seen, its index is
    pushed to the stack. When a close parenthesis is seen, the top most element is popped from the stack. If the stack
    is not empty, the difference between the current index and the index stored at the top of the stack is tracked. If
    the stack is empty, the current index is pushed to the stack. This process continues until all characters in the
    input string are processed. The longest difference is the answer.
    Time complexity: O(n), where n is the length of the input string.
    Space complexity: O(n), as the stack can have up to the length of the input string.

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
                # idx - stack[-1] finds the length of the substring between the current idx and the one at top of the
                # stack
                longest = max(longest, idx - stack[-1])
            else:
                # appending the current idx makes idx - stack[-1] accurate in certain cases
                stack.append(idx)

    return longest
