class Problem4:
    """
    Class for Median of Two Sorted Arrays (#4)
    https://leetcode.com/problems/median-of-two-sorted-arrays/
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Returns the median of two inputted sorted arrays
        Time complexity: O(m+n)
        Space complexity: O(m+n)
           
        :param nums1: the first integer array
        :param nums2: the second integer array
        :return median: the median of the two sorted arrays
        """
        
        # we set the variables m and n equal to the lengths of the arrays nums1 and nums2, respectively
        m = len(nums1)
        n = len(nums2)
        
        # we create an empty array of length (m + n) to fill with the values from nums1 and nums2 once we sort the merged arrays
        merged = [None] * (m + n)

        k = 0
        
        # we're iterating through the arrays and comparing the smallest elements in each array (nums1[0] and nums2[0])
        # we add the smaller of the first elements of the arrays
        while (len(nums1) > 0) and (len(nums2) > 0):
            if nums1[0] < nums2[0]: 
                # once we've found the smaller element, we append it into the merged array
                merged[k] = nums1.pop(0)
                # we increment the index so that we don't overwrite values
                k += 1
            else: # where nums2[0] < nums1[0]
                merged[k] = nums2.pop(0)
                k += 1
                
        # once we've iterated through an entire array, we must copy the remaining elements of the larger array in the same order into the array merged
        # case where m > n
        if len(nums1) > 0: 
            while len(nums1) > 0:
                merged[k] = nums1.pop(0)
                k += 1
                
        # case where m < n
        if len(nums2) > 0:
            while len(nums2) > 0:
                merged[k] = nums2.pop(0)
                k += 1
                
        # x represents the length of the merged array
        x = m + n
        # if the array has an odd number of elements, the median is the middle element
        if x % 2 == 1:
            median = merged[(x - 1)//2]
        # if the array has an even number of elements, the median is the average of the 2 middle elements
        else:
            median = float(merged[x//2 - 1] + merged[x//2])/ 2
        return median
