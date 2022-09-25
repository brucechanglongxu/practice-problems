# https://leetcode.com/problems/first-missing-positive/
def first_missing_positive(nums: list[int]) -> int:
    """
    Finds and returns the smallest missing positive integer in nums
    Algorithm: If the space complexity were O(n), then another boolean list could be made to say whether a value exists.
    We could iterate through this array to find the first False, i.e. the first missing positive. However, this can be
    optimized by keeping only the original list but multiplying each number by -1 if it exists. First, the code turns
    elements that are out of bounds into a fixed number. Then, we implement the encoding and decoding logic mentioned
    previously. Then, it traverses through the array and returns the index of the first positive number if it exists,
    else the length of the input array + 1.
    Time Complexity: O(n), where is the length of nums.
    Space Complexity: O(1).

    :param nums: Unsorted integer array
    :return: smallest missing positive integer in nums
    """
    # make a copy of nums to prevent programming with side effects
    modified_nums = nums.copy()
    num_integers = len(modified_nums)
    # change all elements that are out of the possible range of values to a fixed number
    for idx in range(num_integers):
        if modified_nums[idx] > num_integers or modified_nums[idx] <= 0:
            modified_nums[idx] = num_integers + 1

    for idx in range(num_integers):
        # if the magnitude of the current element is in the possible range of values,
        # then set the new index to the current element
        # and make the element at that new index negative
        if abs(modified_nums[idx]) <= num_integers:
            new_idx = abs(modified_nums[idx]) - 1
            modified_nums[new_idx] = -abs(modified_nums[new_idx])

    # return the first missing positive number if exists in modified_nums
    for idx in range(num_integers):
        if modified_nums[idx] > 0:
            return idx + 1
    return num_integers + 1
