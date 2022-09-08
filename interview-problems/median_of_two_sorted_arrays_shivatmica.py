from math import floor

class Solution:
    """
    Class for Median of Two Sorted Arrays (#4)
    # https://leetcode.com/problems/median-of-two-sorted-arrays/
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Returns the median of two inputted sorted arrays
            
        Parameters
        ----------
        nums1 : List[int]
            The first integer array
        nums2 : List[int]
            The second integer array
            
        Returns
        -------
        median : float
            The median of the two sorted arrays
        """
        m = len(nums1)
        n = len(nums2)
        finalArray = [None] * (m + n)
        i, j, k = 0, 0, 0
        while (i < m) and (j < n):
            if nums1[i] < nums2[j]:
                finalArray[k] = nums1[i]
                k += 1
                i += 1
            else:
                finalArray[k] = nums2[j]
                k += 1
                j += 1
        if i < m:
            while i < m:
                finalArray[k] = nums1[i]
                k += 1
                i += 1
        if j < n:
            while j < n:
                finalArray[k] = nums2[j]
                k += 1
                j += 1

        n = n + m
        if n % 2 == 1:
            return finalArray[floor( floor(n + 1) / 2) - 1]
        else:
            return float((finalArray[(floor(n / 2)) - 1]) + float(finalArray[floor(n / 2)]))/ 2
