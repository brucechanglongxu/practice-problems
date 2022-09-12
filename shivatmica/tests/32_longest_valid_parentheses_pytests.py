from solutions import 32_longest_valid_parentheses

def test_case_1(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 1: Leetcode example test case #1
    Expected output: 2
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "(()"
    assert sol.longest_valid_parentheses(s) == 2

def test_case_2(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 2: Leetcode example test case #2
    Expected output: 4
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = ")()())"
    assert sol.longest_valid_parentheses(s) == 4

def test_case_3(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 3: Leetcode example test case #3
    Expected output: 0
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = ""
    assert sol.longest_valid_parentheses(s) == 0

def test_case_4(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 4: Leetcode example test case #4
    Expected output: 4
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "((())"
    assert sol.longest_valid_parentheses(s) == 4

def test_case_5(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 5: Leetcode example test case #5
    Expected output: 4
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "())((())"
    assert sol.longest_valid_parentheses(s) == 4
    
def test_case_6(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 6: a string with just left parentheses
    Expected output: 0
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "((((("
    assert sol.longest_valid_parentheses(s) == 0    

def test_case_7(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 7: a string with just right parentheses
    Expected output: 0
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = ")))))"
    assert sol.longest_valid_parentheses(s) == 0
    
def test_case_8(sol = 32_longest_valid_parentheses.Problem32()) -> None:
    """
    Test case 8: a string containing the maximum number of parentheses as allowed
    Expected output: 30000
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "(())" * 7500
    assert sol.longest_valid_parentheses(s) == 3 * (10**4)
    
    
def main() -> None:
    """
    Executes each of the test cases
    
    Returns
    -------
    None
    """
    sol = 32_longest_valid_parentheses.Problem32()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)
    test_case_6(sol)
    test_case_7(sol)
    test_case_8(sol)
    
if __name__ == "__main__":
    main()
    print("Accepted solution")
