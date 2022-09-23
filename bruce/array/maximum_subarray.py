# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum

# Brute Force: O(N^2) time 
# The approach is to iterate over all of the possible subarrays
# and return the subarray with the largest sum
class Solution
  def maxSubArrayBF(self, nums: List[int]) -> int:
    maxSum = 0
    maxArray = []
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        currSum = 0
        for k in range(i, j):
          currSum += nums[k]
        if (currSum > maxSum):
          maxArray = nums[i:j]
    return maxArray
  
# Dynamic Programming Solution: O(N) time 
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    dp = []
    dp.append(nums[0])
    current_largest_sum = dp[0]
    for i in range(1, len(nums)):
      dp.append(max(dp[i-1] + nums[i], nums[i]))
      if dp[i] > current_largest_sum:
        current_largest_sum = dp[i]
    return current_largest_sum
