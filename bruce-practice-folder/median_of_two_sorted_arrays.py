class Solution:
 def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    if len(B) < len(A):
       A, B = B, A
    l, r = 0, len(A) - 1
    while True:
       i = (l + r) // 2
       j = half - i - 2
       Aleft = A[i] if i >= 0 else float("-infinity")
       Aright = A[i + 1]
       Bleft = B[j] if j >= 0 else float("-infinity")
       Bright = B[j + 1]
 
