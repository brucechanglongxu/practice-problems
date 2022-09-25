p32 = __import__("32")


def test_case_1() -> None:
    """
    Test case. Create an input string with two consecutive matching parentheses. Note that this is LeetCode example test
    case 1.

    Verify that the longest number of valid parentheses is 2.

    :return: None
    """
    input_str = "(()"
    assert p32.longest_valid_parentheses(input_str) == 2


def test_case_2() -> None:
    """
    Test case. Create an input string four consecutive matching parentheses. Note that this is LeetCode example test
    case 2.

    Verify that the longest number of valid parentheses is 4.

    :return: None
    """
    input_str = ")()())"
    assert p32.longest_valid_parentheses(input_str) == 4


def test_case_3() -> None:
    """
    Test case. Create an empty input string. Note that this is LeetCode example test case 3.

    Verify that the longest number of valid parentheses is 0.

    :return: None
    """
    input_str = ""
    assert p32.longest_valid_parentheses(input_str) == 0


def test_case_4() -> None:
    """
    Test case. Create an input string with only open parentheses.

    Verify that the longest number of valid parentheses is 0.

    :return: None
    """
    input_str = "((((((((("
    assert p32.longest_valid_parentheses(input_str) == 0


def test_case_5() -> None:
    """
    Test case. Create an input string with only closed parentheses.

    Verify that the longest number of valid parentheses is 0.

    :return: None
    """
    input_str = ")))))))))"
    assert p32.longest_valid_parentheses(input_str) == 0


def test_case_6() -> None:
    """
    Test case. Create an input string with the maximum number of parentheses (3 * 10**4). This means 15000 pairs of open
    and close parentheses.

    Verify that the longest number of valid parentheses is 30000.

    :return: None
    """
    input_str = "()" * 15000
    assert p32.longest_valid_parentheses(input_str) == 30000


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


if __name__ == "__main__":
    main()
    print("All tests pass")
