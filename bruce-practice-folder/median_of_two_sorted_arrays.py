class Solution:
 def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
 A, B = nums1, nums2
 total = len(nums1) + len(nums2)
 half = total // 2
 if len(B) < len(A):
  A, B = B, A
 
