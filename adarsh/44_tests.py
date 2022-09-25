p44 = __import__("44")


def test_case_1() -> None:
    """
    Test case. Create an input string and pattern string with distinct characters that don't have the same length. Note
    that this is LeetCode example test case 1.

    Verify that the pattern does not match the string.

    :return: None
    """
    s = "aa"
    p = "a"
    assert p44.is_match(s, p) == False


def test_case_2() -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with only a star. Note that this is
    LeetCode example test case 2.

    Verify that the pattern matches the string.

    :return: None
    """
    s = "aa"
    p = "*"
    assert p44.is_match(s, p) == True


def test_case_3() -> None:
    """
    Test case. Create an input string with distinct characters and the pattern string containing a question mark. Note
    that this is LeetCode example test case 3.

    Verify that the pattern does not match the string.

    :return: None
    """
    s = "cb"
    p = "?a"
    assert p44.is_match(s, p) == False


def test_case_4() -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with multiple stars.

    Verify that the pattern matches the string.

    :return: None
    """
    s = "abcdefg"
    p = "**********"
    assert p44.is_match(s, p) == True


def test_case_5() -> None:
    """
    Test case. Create an input string and pattern string with the same distinct characters.

    Verify that the pattern matches the string.

    :return: None
    """
    s = "abcdefg"
    p = "abcdefg"
    assert p44.is_match(s, p) == True


def test_case_6() -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with all question marks.

    Verify that the pattern matches the string.

    :return: None
    """
    s = "abcdefg"
    p = "???????"
    assert p44.is_match(s, p) == True


def test_case_7() -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with distinct characters, question
    marks, and a star.

    Verify that the pattern matches the string.

    :return: None
    """
    s = "abcdefg"
    p = "??c?e?g*"
    assert p44.is_match(s, p) == True


def test_case_8() -> None:
    """
    Test case. Create an input string with distinct characters and a pattern string with distinct characters, question
    marks, and stars.

    Verify that the pattern does not match the string.

    :return: None
    """
    s = "abcdefg"
    p = "??*h?g*"
    assert p44.is_match(s, p) == False


def test_case_9() -> None:
    """
    Test case. Create an input string and pattern string with empty strings. This tests the low end of the range of
    constraints in the problem.

    Verify that the pattern matches the string.

    :return: None
    """
    s = ""
    p = ""
    assert p44.is_match(s, p) == True


def test_case_10() -> None:
    """
    Test case. Create an input string with 2000 distinct characters and a pattern string with only one star. This tests
    the high end of the range of constraints in the problem.

    Verify that the pattern matches the string.

    :return: None
    """
    s = "z" * 2000
    p = "*"
    assert p44.is_match(s, p) == True


def main() -> None:
    """
    Runs the test cases.

    :return: None
    """
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    test_case_8()
    test_case_9()
    test_case_10()


if __name__ == "__main__":
    main()
    print("All tests pass")
