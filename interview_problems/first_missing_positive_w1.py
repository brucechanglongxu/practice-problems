# Given an unsorted integer array nums, return the smallest missing positive integer
# you must implement an algorithm than runs in O(n) time and uses constant extra space
# https://leetcode.com/problems/first-missing-positive/

# Naive Solution, where we first sort our array
def first_missing_number(nums):
  # If there are no integers in our array, then the smallest
  # missing positive integer is equal to 1
  if len(nums) == 0:
    return 1
  # Sort our array
  nums.sort()
  smallest_int_num = 0
  for i in range(len(nums) - 1):
    if nums[i] <= 0 or nums[i] == nums[i+1]:
      continue
    else:
      if nums[i + 1] - nums[i] != 1:
        smallest_int_num = nums[i] + 1
        return smallest_int_num
  if smallest_int_num == 0:
    smallest_int_num = nums[-1] + 1
    return smallest_int_num
 
