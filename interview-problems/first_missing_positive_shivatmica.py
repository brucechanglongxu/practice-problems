class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # to ensure that the nums array doesn't iterate beyond the given values
        nums.append(0) 
        n = len(nums)
        
        # we don't need to consider negative or zero values (only non-negative integers)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        # updates index i about the value i in the range from 1 to n
        # since we're incrementing by n, we don't change the value (we're using mod n)
        for i in range(n):
            nums[nums[i] % n] += n
            
        # if we never incremented a nums array value, the integer division by n would be 0 (rounded down)
        for i in range(n):
            if (nums[i] // n == 0):
                # we return the smallest particular index that hasn't been incremented (or isn't in the array)
                return i 
              
        # if all other indices are present, the largest number or the number 1 greater than the array's length is missing
        return n
