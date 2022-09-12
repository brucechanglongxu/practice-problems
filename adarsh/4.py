# https://leetcode.com/problems/median-of-two-sorted-arrays/
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Finds and returns the median of two sorted arrays.

    :param nums1: First sorted array
    :param nums2: Second sorted array
    :return: median of the two sorted arrays
    """
    total_length = len(nums1) + len(nums2)
    if total_length % 2 == 0:
        # return the average of the two middle numbers
        return (find_recur(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, total_length // 2 - 1) + find_recur(
            nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, total_length // 2)) / 2
    else:
        # return the middle number
        return find_recur(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, total_length // 2)


def find_recur(nums1: list[int], nums1_start: int, nums1_end: int, nums2: list[int], nums2_start: int, nums2_end: int,
               k: int) -> int:
    """
    Recursively finds and returns the kth smallest element of the combined arrays

    :param nums1: First sorted array
    :param nums1_start: Starting point for nums1
    :param nums1_end: Ending point for nums1
    :param nums2: Second sorted array
    :param nums2_start: Starting point for nums2
    :param nums2_end: Ending point for nums2
    :param k: relative smallest element (i.e. 1 for 1st smallest, 2 for 2nd smallest, etc.)
    :return: kth smallest element of the combined arrays
    """
    # if either of the lists is empty then the kth smallest element of the combined arrays is returned
    if nums1_end < nums1_start:
        return nums2[k + nums2_start]
    if nums2_end < nums2_start:
        return nums1[k + nums1_start]

    # initialize starting indices, lengths, and medians of nums1 and nums2
    nums1_idx, nums2_idx = (nums1_start + nums1_end) // 2, (nums2_start + nums2_end) // 2
    nums1_length, nums2_length = nums1_idx - nums1_start, nums2_idx - nums2_start
    nums1_median, nums2_median = nums1[nums1_idx], nums2[nums2_idx]

    # if combined length is too large, remove the end of the list with the larger median
    if nums1_length + nums2_length >= k:
        if nums1_median <= nums2_median:
            return find_recur(nums1, nums1_start, nums1_end, nums2, nums2_start, nums2_idx - 1, k)
        else:
            return find_recur(nums1, nums1_start, nums1_idx - 1, nums2, nums2_start, nums2_end, k)
    # else combined length is too small and we need to remove the beginning of the list with the smaller median
    else:
        if nums1_median <= nums2_median:
            return find_recur(nums1, nums1_idx + 1, nums1_end, nums2, nums2_start, nums2_end, k - nums1_length - 1)
        else:
            return find_recur(nums1, nums1_start, nums1_end, nums2, nums2_idx + 1, nums2_end, k - nums2_length - 1)
