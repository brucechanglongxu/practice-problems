from interview_problems import first_missing_positive_adarsh


def test_case_1(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with 0 and the first two smallest positive integers. Note that this is LeetCode example test case 1.

    Verify that the smallest missing positive integer in that array is 3.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [1, 2, 0]
    assert sol.first_missing_positive(nums) == 3


def test_case_2(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with -1 and the first four smallest positive integers except two. Note that this is LeetCode example test case 2.

    Verify that the smallest missing positive integer in that array is 2.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [3, 4, -1, 1]
    assert sol.first_missing_positive(nums) == 2


def test_case_3(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with five positive integers that are out of range. Note that this is LeetCode example test case 3.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [7, 8, 9, 11, 12]
    assert sol.first_missing_positive(nums) == 1


def test_case_4(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with -1 and two positive integers that are out of range.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [-1, 10, 15]
    assert sol.first_missing_positive(nums) == 1


def test_case_5(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with the first three smallest positive integers.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [1, 2, 3]
    assert sol.first_missing_positive(nums) == 4


def test_case_6(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with -1, 0, and the first five smallest positive integers.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [1, 2, 3, 4, 5, -1, 0]
    assert sol.first_missing_positive(nums) == 6


def test_case_7(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with 0 and the unsorted first two smallest positive integers.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [2, 1, 0]
    assert sol.first_missing_positive(nums) == 3


def test_case_8(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with two of the same positive integer.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [2, 2]
    assert sol.first_missing_positive(nums) == 1


def test_case_9(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with 0, two ones, and two twos.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [0, 2, 2, 1, 1]
    assert sol.first_missing_positive(nums) == 3


def test_case_10(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with all zeros.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [0, 0, 0]
    assert sol.first_missing_positive(nums) == 1


def test_case_11(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with only -1.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [-1]
    assert sol.first_missing_positive(nums) == 1


def test_case_12(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with only 1.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [1]
    assert sol.first_missing_positive(nums) == 2


def test_case_13(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with maximum allowed length (10**5).

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [num for num in range(1, 10**5 + 1)]
    assert sol.first_missing_positive(nums) == 10**5 + 1


def test_case_14(sol: first_missing_positive_adarsh.Solution) -> None:
    """
    Test case. Create an unsorted integer array with the lowest and highest allowed integers.

    Verify that the smallest missing positive integer in that array is 1.

    :param sol: Object with first_missing_positive solution method
    :return: None
    """
    nums = [-(2**31), 2**31 - 1]
    assert sol.first_missing_positive(nums) == 1


def main() -> None:
    """
    Runs the test cases.

    :return: None
    """
    sol = first_missing_positive_adarsh.Solution()
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
    test_case_11(sol)
    test_case_12(sol)
    test_case_13(sol)
    test_case_14(sol)


if __name__ == "__main__":
    main()
    print("All tests pass")
