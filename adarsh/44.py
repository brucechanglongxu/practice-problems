# https://leetcode.com/problems/wildcard-matching/
def is_match(
        s: str = "aa",
        p: str = "a",
) -> bool:
    """
    Finds and returns whether the pattern p matches the entire input string s.
    Algorithm: This code uses a dynamic programming approach. It uses an array, dp, with each element being True or
    False, representing whether the first idx elements of s can be matched. It works backwards through dp to update each
    element. If the strings match, then the last element is True, otherwise False. There are three cases for
    corresponding characters in s and p: they are the same character, the character in p is a ?, or the character in p
    is a *. This program goes through each of those possible cases and updates dp accordingly.
    Time Complexity: O(mn), where m is the length of p and n is the length of s.
    Space Complexity: O(n), where n is the length of s.

    :param s: Input string consisting of only lowercase English letters
    :param p: Pattern consisting of only lowercase English letters, '?', or '*'
    :return: bool representing whether the pattern p matches the entire input string s
    """
    s_length = len(s)
    # dp[idx] stores whether we can match the first idx elements of s
    # 0,0 is always True and everything else will initially be False
    dp = [False] * s_length
    dp.insert(0, True)

    # first_position holds the first index with True
    first_position = 0
    for char in p:
        # if we can fill multiple elements
        if char == "*":
            # all elements after the first True can turn True as well
            for idx in range(first_position, s_length + 1):
                dp[idx] = True
        # else we can fill only the current element
        else:
            first_position = s_length + 2
            # we go in reverse order to avoid overwriting values and subsequently accessing the wrong ones
            for idx in reversed(range(s_length)):
                # check whether the current idx matches
                dp[idx + 1] = (char == "?" or char == s[idx]) and dp[idx]
                if dp[idx + 1]:
                    # going in reverse order allows us to keep updating in this way
                    first_position = idx + 1
        dp[0] = char == "*" and dp[0]
    # return the last element in dp since that is len(s), len(p)
    return dp[-1]
