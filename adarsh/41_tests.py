p41 = __import__("41")


def test_case_1() -> None:
    """
    Test case. Create an unsorted integer array with 0 and the first two smallest positive integers. Note that this is LeetCode example test case 1.

    Verify that the smallest missing positive integer in that array is 3.

    :return: None
    """
    nums = [1, 2, 0]
    assert p41.first_missing_positive(nums) == 3


def test_case_2() -> None:
    """
    Test case. Create an unsorted integer array with -1 and the first four smallest positive integers except the number two. Note that this is LeetCode example test case 2.

    Verify that the smallest missing positive integer in that array is 2.

    :return: None
    """
    nums = [3, 4, -1, 1]
    assert p41.first_missing_positive(nums) == 2


def test_case_3() -> None:
    """
    Test case. Create a sorted integer array with five positive integers that are out of range. Note that this is LeetCode example test case 3.

    Verify that the smallest missing positive integer in that array is 1.

    :return: None
    """
    nums = [7, 8, 9, 11, 12]
    assert p41.first_missing_positive(nums) == 1


def test_case_4() -> None:
    """
    Test case. Create a sorted integer array with -1 and two positive integers that are out of range.

    Verify that the smallest missing positive integer in that array is 1.

    :return: None
    """
    nums = [-1, 10, 15]
    assert p41.first_missing_positive(nums) == 1


def test_case_5() -> None:
    """
    Test case. Create an unsorted integer array with the first three smallest positive integers.

    Verify that the smallest missing positive integer in that array is 4.

    :return: None
    """
    nums = [1, 2, 3]
    assert p41.first_missing_positive(nums) == 4


def test_case_6() -> None:
    """
    Test case. Create an unsorted integer array with -1, 0, and the first five smallest positive integers.

    Verify that the smallest missing positive integer in that array is 6.

    :return: None
    """
    nums = [1, 2, 3, 4, 5, -1, 0]
    assert p41.first_missing_positive(nums) == 6


def test_case_7() -> None:
    """
    Test case. Create an unsorted integer array with 0 and the unsorted first two smallest positive integers.

    Verify that the smallest missing positive integer in that array is 3.

    :return: None
    """
    nums = [2, 1, 0]
    assert p41.first_missing_positive(nums) == 3


def test_case_8() -> None:
    """
    Test case. Create an integer array with two of the same positive integer.

    Verify that the smallest missing positive integer in that array is 1.

    :return: None
    """
    nums = [2, 2]
    assert p41.first_missing_positive(nums) == 1


def test_case_9() -> None:
    """
    Test case. Create an unsorted integer array with 0, two ones, and two twos.

    Verify that the smallest missing positive integer in that array is 3.

    :return: None
    """
    nums = [0, 2, 2, 1, 1]
    assert p41.first_missing_positive(nums) == 3


def test_case_10() -> None:
    """
    Test case. Create an integer array with all zeros.

    Verify that the smallest missing positive integer in that array is 1.

    :return: None
    """
    nums = [0, 0, 0]
    assert p41.first_missing_positive(nums) == 1


def test_case_11() -> None:
    """
    Test case. Create an integer array with only -1.

    Verify that the smallest missing positive integer in that array is 1.

    :return: None
    """
    nums = [-1]
    assert p41.first_missing_positive(nums) == 1


def test_case_12() -> None:
    """
    Test case. Create an unsorted integer array with only 1.

    Verify that the smallest missing positive integer in that array is 2.

    :return: None
    """
    nums = [1]
    assert p41.first_missing_positive(nums) == 2


def test_case_13() -> None:
    """
    Test case. Create an sorted integer array with maximum allowed length (10**5).

    Verify that the smallest missing positive integer in that array is higher than the maximum allowed length (10**5 + 1).

    :return: None
    """
    nums = [num for num in range(1, 10 ** 5 + 1)]
    assert p41.first_missing_positive(nums) == 10 ** 5 + 1


def test_case_14() -> None:
    """
    Test case. Create an unsorted integer array with the lowest and highest allowed integers.

    Verify that the smallest missing positive integer in that array is 1.

    :return: None
    """
    nums = [-(2 ** 31), 2 ** 31 - 1]
    assert p41.first_missing_positive(nums) == 1


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
    test_case_7()
    test_case_8()
    test_case_9()
    test_case_10()
    test_case_11()
    test_case_12()
    test_case_13()
    test_case_14()


if __name__ == "__main__":
    main()
    print("All tests pass")
