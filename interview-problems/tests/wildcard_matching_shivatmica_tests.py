
from interview_problems import wildcard_matching_shivatmica

def test_case_1(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 1: both the sequence and the pattern are empty strings
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = ""
    p = ""
    assert sol.wildcard_matching_shivatmica(s, p) == True
    
def test_case_2(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 2: a string of characters compared to the pattern with only stars
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "testcase"
    p = "****"
    assert sol.wildcard_matching_shivatmica(s, p) == True
    
def test_case_3(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 3: a string of characters compared to a pattern with an equivalent number of question marks
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "testcase"
    p = "????????"
    assert sol.wildcard_matching_shivatmica(s, p) == True

def test_case_4(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 4: a string of characters compared to a pattern with the same characters
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "testcase"
    p = "testcase"
    assert sol.wildcard_matching_shivatmica(s, p) == True
    
def test_case_5(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 5: a string of characters compared to a pattern with some characters, stars, and question marks
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "testcase"
    p = "*e?t?ca??"
    assert sol.wildcard_matching_shivatmica(s, p) == True 
    
def test_case_6(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 6: a string with the maximum number of possible characters and a pattern of a string of stars
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "a" * 2000
    p = "***"
    assert sol.wildcard_matching_shivatmica(s, p) == True
    

def test_case_7(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 7: Leetcode example test case #1
    Expected output: False
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "aa"
    p = "a"
    assert sol.wildcard_matching_shivatmica(s, p) == False

def test_case_8(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 8: Leetcode example test case #2
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "aa"
    p = "*"
    assert sol.wildcard_matching_shivatmica(s, p) == True
    
def test_case_9(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 9: Leetcode example test case #3
    Expected output: False
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "cb"
    p = "?a"
    assert sol.wildcard_matching_shivatmica(s, p) == False
    
def test_case_10(sol: wildcard_matching_shivatmica.Solution) -> None:
    """
    Test case 10: Leetcode example test case #4
    Expected output: True
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    s = "adceb"
    p = "*a*b"
    assert sol.wildcard_matching_shivatmica(s, p) == True

def main() -> None:
    """
    Executes each of the test cases
    
    Returns
    -------
    None
    """
    sol = wildcard_matching_shivatmica.Solution()
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
    print("Accepted solution")
