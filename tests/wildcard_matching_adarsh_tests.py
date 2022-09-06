from interview_problems import wildcard_matching_adarsh


def test_case_1(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string and pattern string with distinct characters that don't have the same length. Note that this is LeetCode example test case 1.

    Verify that the pattern does not match the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "aa"
    p = "a"
    assert sol.is_match(s, p) == False


def test_case_2(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with only a star. Note that this is LeetCode example test case 2.

    Verify that the pattern matches the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "aa"
    p = "*"
    assert sol.is_match(s, p) == True


def test_case_3(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string with distinct characters and the pattern string containing a question mark. Note that this is LeetCode example test case 3.

    Verify that the pattern does not match the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "cb"
    p = "?a"
    assert sol.is_match(s, p) == False


def test_case_4(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with multiple stars.

    Verify that the pattern matches the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcdefg"
    p = "**********"
    assert sol.is_match(s, p) == True


def test_case_5(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string and pattern string with the same distinct characters.

    Verify that the pattern matches the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcdefg"
    p = "abcdefg"
    assert sol.is_match(s, p) == True


def test_case_6(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with all question marks.

    Verify that the pattern matches the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcdefg"
    p = "???????"
    assert sol.is_match(s, p) == True


def test_case_7(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with distinct characters, question marks, and a star.

    Verify that the pattern matches the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcdefg"
    p = "??c?e?g*"
    assert sol.is_match(s, p) == True


def test_case_8(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with distinct characters, question marks, and stars.

    Verify that the pattern does not match the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcdefg"
    p = "??*h?g*"
    assert sol.is_match(s, p) == False


def test_case_9(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string and pattern string with empty strings. This tests the low end of the range of constraints in the problem.

    Verify that the pattern matches the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = ""
    p = ""
    assert sol.is_match(s, p) == True


def test_case_10(sol: wildcard_matching_adarsh.Solution) -> None:
    """
    Test case. Create an input string with 2000 distinct characters and a pattern string with only one star. This tests the high end of the range of constraints in the problem.

    Verify that the pattern matches the string.

    :param sol: Object with is_match solution method
    :return: None
    """
    s = "z" * 2000
    p = "*"
    assert sol.is_match(s, p) == True


def main() -> None:
    """
    Runs the test cases.

    :return: None
    """
    sol = wildcard_matching_adarsh.Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)
    test_case_6(sol)
    test_case_7(sol)
    test_case_8(sol)
    test_case_9(sol)
    test_case_10(sol)


if __name__ == "__main__":
    main()
    print("All tests pass")
