# Q: Given an array of integers nums, and an integer target, return the indices
# of the two numbers such that they add up to target

# Brute Force Solution: O(n^2) time complexity, O(1) space complexity
def twoNumberSum(array, targetSum):
  # Iterate over all pairs of elements within the array
  for i in range(0, len(array)):
    for j in range(i+1, len(array)):
      # Check if the sum of the pairs of elements is equal to target sum
      if array[i] + array[j] == targetSum:
        return ([array[i], array[j]])
  # If none of the sums is equal to target sum by the end of the loop then return empty
  return []

# Hashmap Solution: O(n) time complexity, O(n) space complexity
def twoNumberSum(array, targetSum):
  matches = {}
  for number in array:
    match = targetSum - number
    if match in matches:
      return [match, number]
    else:
      matches[number] = True
  return []

# Double Pointer Solution: O(n log n) time complexity, O(1) space complexity
def twoNumberSum(array, targetSum):
  array.sort()
  left = 0
  right = len(array) - 1
  while left < right:
    if array[left] + array[right] == targetSum:
      return [array[left], array[right]]
    elif array[left] + array[right] < targetSum:
      left += 1
    elif array[left] + array[right] > targetSum:
      right -= 1
  return []
