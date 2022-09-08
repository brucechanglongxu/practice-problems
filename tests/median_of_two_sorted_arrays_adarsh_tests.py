from interview_problems import median_of_two_sorted_arrays_adarsh


def test_case_1(sol: median_of_two_sorted_arrays_adarsh.Solution) -> None:
    """
    Test case. Create the first sorted integer array with elements that are less than and more than those in the second array. Note that this is LeetCode example test case 1.

    Verify that the median of these two sorted arrays is 2.

    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [1, 3]
    nums2 = [2]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 2


def test_case_2(sol: median_of_two_sorted_arrays_adarsh.Solution) -> None:
    """
    Test case. Create the first sorted integer array with elements that are less than those in the second array. Note that this is LeetCode example test case 2.

    Verify that the median of these two sorted arrays is 2.5.

    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 2.5


def test_case_3(sol: median_of_two_sorted_arrays_adarsh.Solution) -> None:
    """
    Test case. Create the first sorted integer array and make the second array an empty array.

    Verify that the median of these two sorted arrays is 1.5.

    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [1, 2]
    nums2 = []
    assert sol.find_median_sorted_arrays(nums1, nums2) == 1.5


def test_case_4(sol: median_of_two_sorted_arrays_adarsh.Solution) -> None:
    """
    Test case. Create the first array to be an empty array and the second array to be a sorted integer array.

    Verify that the median of these two sorted arrays is 7.5.

    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = []
    nums2 = [3, 12]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 7.5


def test_case_5(sol: median_of_two_sorted_arrays_adarsh.Solution) -> None:
    """
    Test case. Create the first array to be the low end of the range of values given in the LeetCode problem (-10**6) and the second array to be the high end of the range of values given in the LeetCode problem (10**6).

    Verify that the median of these two sorted arrays is 0.

    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [-(10**6)]
    nums2 = [10**6]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 0


def test_case_6(sol: median_of_two_sorted_arrays_adarsh.Solution) -> None:
    """
    Test case. Create the first sorted array with 1000 elements (with values from 0 through 999) and the second sorted array with 1000 elements (with values from 2000 through 2999) to test the maximum number of elements allowed in each input array.

    Verify that the median of these two sorted arrays is 1499.5.

    :param sol: Object with find_median_sorted_arrays solution method
    :return: None
    """
    nums1 = [num for num in range(0, 1000)]
    nums2 = [num for num in range(2000, 3000)]
    assert sol.find_median_sorted_arrays(nums1, nums2) == 1499.5


def main() -> None:
    """
    Runs the test cases.

    :return: None
    """
    sol = median_of_two_sorted_arrays_adarsh.Solution()
    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)
    test_case_4(sol)
    test_case_5(sol)
    test_case_6(sol)


if __name__ == "__main__":
    main()
    print("All tests pass")
