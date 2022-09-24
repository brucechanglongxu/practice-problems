import longest_valid_parentheses

def first_test_case(sol: longest_valid_parentheses.Solution) -> None:
    """
    Test for an empty string
    :return: None
    """
    input_str = ""
    assert sol.longest_valid_parentheses(input_str) == 0
    
def second_test_case(sol: longest_valid_parentheses.Solution) -> None:
    """
    A singular pair of parentheses. 
    :return: None
    """
    input_str = "()"
    assert sol.longest_valid_parentheses(input_str) == 2
    
def third_test_case(sol: longest_valid_parentheses.Solution) -> None:
    """
    Two pairs of parentheses, interleaved. 
    :return: None
    """
    input_str = "(())"
    assert sol.longest_valid_parentheses(input_str) == 4
    
def fourth_test_case(sol: longest_valid_parentheses.Solution) -> None:
    """
    Two pairs of parentheses, adjacent. 
    :return: None
    """
    input_str = "()()"
    assert sol.longest_valid_parentheses(input_str) == 4

def main() -> None:
    """
    Runs the test cases.
    :return: None
    """
    sol = longest_valid_parentheses.Solution()
    first_test_case(sol)
    second_test_case(sol)
    third_test_case(sol)
    fourth_test_case(sol)

if __name__ == "__main__":
    main()
    print("Our solution passes")
