from interview_problems import median_two_sorted_arrays_shivatmica

def test_case_1(sol = median_two_sorted_arrays_shivatmica.Solution()) -> None:
    """
    Test case 1: Leetcode example test case #1
    Expected output: 2.00000
    
    Parameters
    ----------
    sol : object
        consists of the median_two_sorted_arrays question's solution
        
    Returns
    -------
    None
    """
    nums1 = [1, 3]
    nums2 = [2]
    assert sol.findMedianSortedArrays(nums1, nums2) == 2.00000

def test_case_2(sol = median_two_sorted_arrays_shivatmica.Solution()) -> None:
    """
    Test case 2: Leetcode example test case #2
    Expected output: 2.50000
    
    Parameters
    ----------
    sol : object
        consists of the median_two_sorted_arrays question's solution
        
    Returns
    -------
    None
    """
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert sol.findMedianSortedArrays(nums1, nums2) == 2.50000
    
def test_case_3(sol = median_two_sorted_arrays_shivatmica.Solution()) -> None:
    """
    Test case 3: nums1 array contains the minimum number in the range of possible values for nums1 and nums2 contains the maximum possible number
    Expected output: 0
    
    Parameters
    ----------
    sol : object
        consists of the median_two_sorted_arrays question's solution
        
    Returns
    -------
    None
    """
    nums1 = [-(10**6)]
    nums2 = [10**6]
    assert sol.findMedianSortedArrays(nums1, nums2) == 0
    
def test_case_4(sol = median_two_sorted_arrays_shivatmica.Solution()) -> None:
    """
    Test case 4: the sorted arrays nums1 and nums2 both contain the maximum amount of elements possible in the arrays
    Expected output: 1000.5
    
    Parameters
    ----------
    sol : object
        consists of the median_two_sorted_arrays question's solution
        
    Returns
    -------
    None
    """
    nums1 = list(range(1, 1001))
    nums2 = list(range(1001, 2001))
    assert sol.findMedianSortedArrays(nums1, nums2) == 1000.5
    
def test_case_5(sol = median_two_sorted_arrays_shivatmica.Solution()) -> None:
    """
    Test case 5: nums1 array doesn't contain any elements but nums2 is a sorted array with 6 elements
    Expected output: 7.00000
    
    Parameters
    ----------
    sol : object
        consists of the median_two_sorted_arrays question's solution
        
    Returns
    -------
    None
    """
    nums1 = []
    nums2 = [2, 4, 6, 8, 10, 12]
    assert sol.findMedianSortedArrays(nums1, nums2) == 7.00000
    
def test_case_6(sol = median_two_sorted_arrays_shivatmica.Solution()) -> None:
    """
    Test case 6: nums1 is a sorted array with 6 elements and the nums2 array doesn't contain any elements
    Expected output: 7.00000
    
    Parameters
    ----------
    sol : object
        consists of the median_two_sorted_arrays question's solution
        
    Returns
    -------
    None
    """
    nums1 = [2, 4, 6, 8, 10, 12]
    nums2 = []
    assert sol.findMedianSortedArrays(nums1, nums2) == 7.00000
    
def test_case_7(sol = median_two_sorted_arrays_shivatmica.Solution()) -> None:
    """
    Test case 7: nums1 and nums2 are sorted arrays with 1000 elements each, containing the odd and even numbers respectively
    Expected output: 1000.5
    
    Parameters
    ----------
    sol : object
        consists of the median_two_sorted_arrays question's solution
        
    Returns
    -------
    None
    """
    nums1 = list(range(1, 2001, 2))
    nums2 = list(range(2, 2002, 2))
    assert sol.findMedianSortedArrays(nums1, nums2) == 1000.5
    
def main() -> None:
    """
    Executes each of the test cases
    
    Returns
    -------
    None
    """
    sol = median_two_sorted_arrays_shivatmica.Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)
    test_case_6(sol)
    test_case_7(sol)

if __name__ == "__main__":
    main()
    print("Accepted solution")
