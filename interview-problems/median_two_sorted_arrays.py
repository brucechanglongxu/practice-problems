class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds and returns the median of two sorted arrays.

        :param nums1: First sorted array
        :param nums2: Second sorted array
        :return: median of the two sorted arrays
        """
        len1, len2 = len(nums1), len(nums2)
        # these indices will point to the current smallest values in each array
        nums1_idx = nums2_idx = 0
        # since we sort the values in the arrays as we go, these variables hold the two largest values we've seen so far
        first_largest = second_largest = 0

        # iterate until we reach the middle of the merged array
        for _ in range((len1 + len2) // 2 + 1):
            # since we are going to modify the largest value we've seen, it now becomes the second largest
            second_largest = first_largest
            # passing these conditions indicates that the next highest number is in nums1
            if nums2_idx == len2 or (
                nums1_idx != len1 and nums1[nums1_idx] <= nums2[nums2_idx]
            ):
                first_largest = nums1[nums1_idx]
                nums1_idx += 1
            # reaching here indicates that the next highest number is in nums2
            else:
                first_largest = nums2[nums2_idx]
                nums2_idx += 1

        # return the average of the two largest values if the merged array has an even number of elements, else return the largest value
        return (
            (first_largest + second_largest) / 2
            if (len1 + len2) % 2 == 0
            else first_largest
        )
