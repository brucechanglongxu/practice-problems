from interview_problems_adarsh import longest_valid_parentheses


def test_case_1(sol: longest_valid_parentheses.Solution) -> None:
    """
    Test case. Create an input string with two consecutive matching parentheses. Note that this is LeetCode example test case 1.

    Verify that the longest number of valid parentheses is 2.

    :param sol: Object with longest_valid_parentheses solution method
    :return: None
    """
    input_str = "(()"
    assert sol.longest_valid_parentheses(input_str) == 2


def test_case_2(sol: longest_valid_parentheses.Solution) -> None:
    """
    Test case. Create an input string four consecutive matching parentheses. Note that this is LeetCode example test case 2.

    Verify that the longest number of valid parentheses is 4.

    :param sol: Object with longest_valid_parentheses solution method
    :return: None
    """
    input_str = ")()())"
    assert sol.longest_valid_parentheses(input_str) == 4


def test_case_3(sol: longest_valid_parentheses.Solution) -> None:
    """
    Test case. Create an empty input string. Note that this is LeetCode example test case 3.

    Verify that the longest number of valid parentheses is 0.

    :param sol: Object with longest_valid_parentheses solution method
    :return: None
    """
    input_str = ""
    assert sol.longest_valid_parentheses(input_str) == 0


def test_case_4(sol: longest_valid_parentheses.Solution) -> None:
    """
    Test case. Create an input string with only open parentheses.

    Verify that the longest number of valid parentheses is 0.

    :param sol: Object with longest_valid_parentheses solution method
    :return: None
    """
    input_str = "((((((((("
    assert sol.longest_valid_parentheses(input_str) == 0


def test_case_5(sol: longest_valid_parentheses.Solution) -> None:
    """
    Test case. Create an input string with only closed parentheses.

    Verify that the longest number of valid parentheses is 0.

    :param sol: Object with longest_valid_parentheses solution method
    :return: None
    """
    input_str = ")))))))))"
    assert sol.longest_valid_parentheses(input_str) == 0


def test_case_6(sol: longest_valid_parentheses.Solution) -> None:
    """
    Test case. Create an input string with the maximum number of parentheses (3 * 10**4). This means 15000 pairs of open and close parentheses.

    Verify that the longest number of valid parentheses is 30000.

    :param sol: Object with longest_valid_parentheses solution method
    :return: None
    """
    input_str = "()" * 15000
    assert sol.longest_valid_parentheses(input_str) == 30000


def main() -> None:
    """
    Runs the test cases.

    :return: None
    """
    sol = longest_valid_parentheses.Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)
    test_case_6(sol)


if __name__ == "__main__":
    main()
    print("All tests pass")
