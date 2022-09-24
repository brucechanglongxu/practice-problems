import median_of_two_sorted_arrays


def test_case_1(sol: median_of_two_sorted_arrays.Solution) -> None:
    """
    Test case. Compare two identically sorted arrays. Median should be the median of original array. 
    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 4


def test_case_2(sol: median_of_two_sorted_arrays.Solution) -> None:
    """
    Test case. Compare an array with a 2-element subarray of itself. 
    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [1, 2]
    nums2 = [1, 2, 3, 4, 5]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 2


def test_case_3(sol: median_of_two_sorted_arrays.Solution) -> None:
    """
    Test case. Comparison with an empty array
    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [1, 2, 3, 4, 5]
    nums2 = []
    assert sol.find_median_sorted_arrays(nums1, nums2) == 3


def test_case_4(sol: median_of_two_sorted_arrays.Solution) -> None:
    """
    Test case. Comparison of two sorted arrays that are entirely disjoint
    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [1, 2, 3]
    nums2 = [4, 5]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 3


def test_case_5(sol: median_of_two_sorted_arrays.Solution) -> None:
    """
    Test case. Comparison of arrays with negative numbers 
    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [-1, 2, 3, 4, 5]
    nums2 = [-1, 6]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 3


def main() -> None:
    """
    Runs the test cases.
    :return: None
    """
    sol = median_of_two_sorted_arrays.Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)

if __name__ == "__main__":
    main()
    print("Our solution passes")
