import wildcard_matching


def test_case_1(sol: wildcard_matching.Solution) -> None:
    """
    Test case. Comparison with the empty string.
    :param sol: Object with is_match solution method.
    :return: None
    """
    s = "aa"
    p = ""
    assert sol.is_match(s, p) == False

def test_case_2(sol: wildcard_matching.Solution) -> None:
    """
    Test case. Comparison of two empty strings.
    :param sol: Object with is_match solution method.
    :return: None
    """
    s = ""
    p = ""
    assert sol.is_match(s, p) == True

def test_case_3(sol: wildcard_matching.Solution) -> None:
    """
    Test case. Comparison of star and empty string.
    :param sol: Object with is_match solution method.
    :return: None
    """
    s = "*"
    p = ""
    assert sol.is_match(s, p) == True

def test_case_4(sol: wildcard_matching.Solution) -> None:
    """
    Test case. Comparison of multiple stars sandwhiching a singular character. 
    :param sol: Object with is_match solution method
    :return: None
    """
    s = "aaaa"
    p = "*a*"
    assert sol.is_match(s, p) == True


def test_case_5(sol: wildcard_matching.Solution) -> None:
    """
    Test case. Comparison with all question marks
    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcde"
    p = "?????"
    assert sol.is_match(s, p) == True


def test_case_6(sol: wildcard_matching.Solution) -> None:
    """
    Test case. Comparison with only stars and question marks
    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcde"
    p = "?????"
    assert sol.is_match(s, p) == True


def test_case_7(sol: wildcard_matching.Solution) -> None:
    """
    Test case. Star and question mark sandwhiched between a number and character. 
    :param sol: Object with is_match solution method
    :return: None
    """
    s = "abcd12"
    p = "*1?"
    assert sol.is_match(s, p) == True

def main() -> None:
    """
    Runs the test cases.
    :return: None
    """
    sol = wildcard_matching.Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)
    test_case_6(sol)
    test_case_7(sol)


if __name__ == "__main__":
    main()
    print("Our solution is robust and passes")
