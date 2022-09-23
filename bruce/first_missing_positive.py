def segregate(arr, size):
    j = 0
    for i in range(size):
        if (arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1 # increment count of non-positive integers
    return j
 
 
''' Find the smallest positive missing number
in an array that contains all positive integers '''
def findMissingPositive(arr, size):
    # Mark arr[i] as visited by
    # making arr[arr[i] - 1] negative.
    # Note that 1 is subtracted
    # because index start
    # from 0 and positive numbers start from 1
    for i in range(size):
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
             
    # Return the first index value at which is positive
    for i in range(size):
        if (arr[i] > 0):
             
            # 1 is added because indexes start from 0
            return i + 1
    return size + 1
 
''' Find the smallest positive missing
number in an array that contains
both positive and negative integers '''
def findMissing(arr, size):
    # First separate positive and negative numbers
    shift = segregate(arr, size)
    # Shift the array and call findMissingPositive for
    # positive part
    return findMissingPositive(arr[shift:], size - shift)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Append 0 so that we do not return this as the minimum positive integer
        nums.append(0)
        # Obtain the length of our array
        N = len(nums)
        arr = [0 for _ in range(N)]
        # Iterate through all the numbers in our array, and add onto our returned array
        for i in range(N):
            if 0 < nums[i] <= N:
                arr[nums[i] - 1] += 1
        for i in range(N):
            if arr[i] == 0: return i + 1
