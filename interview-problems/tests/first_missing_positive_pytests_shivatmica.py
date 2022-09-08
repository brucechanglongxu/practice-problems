from interview_problems import first_missing_positive_shivatmica


def test_case_1(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 1: an array with only zeroes
    Expected output: 1
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [0, 0, 0]
    assert sol.firstMissingPositive(nums) == 1

def test_case_2(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 2: an array with just the number 1 and -1
    Expected output: 2
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [1, -1]
    assert sol.firstMissingPositive(nums) == 2

def test_case_3(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 3: an array with two of the same positive number (greater than 1)
    Expected output: 1
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [7, 7]
    assert sol.firstMissingPositive(nums) == 1

def test_case_4(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 4: an array with the first 5 consecutive positive integers (i.e. from 1 to 5)
    Expected output: 6
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [1, 2, 3, 4, 5]
    assert sol.firstMissingPositive(nums) == 6

def test_case_5(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 5: unsorted array including positive and negative integers
    Expected output: 2
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [-3, 5, -2, 0, -1, -4, 4, 3, 1]
    assert sol.firstMissingPositive(nums) == 2

def test_case_6(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 6: an array containing the maximum number of elements allowed
    Expected output: 10**5 (since the array only covers integers until 10**5 - 1
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = list(range(10**5))
    assert sol.firstMissingPositive(nums) == 10**5

def test_case_7(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 7: an array including the boundary cases (testing both sides of the range allowed for any nums[i])
    Expected output: 2
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [-(2**31), (2**31) - 1, 3, 1, 4]
    assert sol.firstMissingPositive(nums) == 2

def test_case_8(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 8: Leetcode example test case #1
    Expected output: 1
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [1, 2, 0]
    assert sol.firstMissingPositive(nums) == 3

def test_case_9(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 9: Leetcode example test case #2
    Expected output: 2
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [3, 4, -1, 1]
    assert sol.firstMissingPositive(nums) == 2

def test_case_10(sol = first_missing_positive_shivatmica.Solution()) -> None:
    """
    Test case 10: Leetcode example test case #3
    Expected output: 1
    
    Parameters
    ----------
    sol : object
        consists of the first_missing_positive question's solution
        
    Returns
    -------
    None
    """
    nums = [7, 8, 9, 11, 12]
    assert sol.firstMissingPositive(nums) == 1

def main() -> None:
    """
    Executes each of the test cases
    
    Returns
    -------
    None
    """
    sol = first_missing_positive_shivatmica.Solution()
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
