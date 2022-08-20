class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # O( (m + n) log (m + n)) -> O(log (m + n))
        # An even number of elements m + n is even
        # [e1, e2], [f1, f2] --> [e1, f1, e2, f2]
        fullnums = nums1 + nums2
        fullnums.sort()
        x = len(fullnums) // 2
        if len(fullnums) % 2 == 0:
            z = (fullnums[x] + fullnums[x - 1]) // 2
            return z
        else:
            z = fullnums[x]
            return z

        # Linear time solution 
        # [1, 2, 4] and [3, 5, 6]
        # Store some intermediate values that will help us keep track of whether we have reached the median or not
        # There is one such value for each of the two arrays 
        # We keep an index for array 1, and keep an index for array 2
        # And we compare the element and each of indexes for their respective arrays
        # and increment the index for which we obtain the smaller element
        # and iterate until we have made (m + n) / 2 comparisons
        
        # 1. What happens if the arrays *aren't sorted*, what is the best time complexity we can achieve in this case?
        # 2. Think about how you would implement this solution above in you language of choice
        # 3. How would we push this further to O(log (m + n))
        
