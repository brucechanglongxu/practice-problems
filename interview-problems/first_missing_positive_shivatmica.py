class Solution:
    """
    Class for First Missing Positive (#41)
    # https://leetcode.com/problems/first-missing-positive/
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Returns the smallest positive number that isn't included in the inputted list
            
        Parameters
        ----------
        nums : List[int]
            The inputted list, an unsorted integer array
            
        Returns
        -------
        i : int
            The index of the first missing positive number
        """
        
        # adding 0 to the end of the list in the case that all the numbers are consecutive and smallest positive numbers
        # the function will then return the value that is greater than all of these values
        nums.append(0) 
        n = len(nums)
        
        # we don't need to consider negative or zero values (only non-negative integers)
        # we can change any irrelevant values that are greater than n to be 0 so they aren't checked 
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        # updates index i about the value i in the range from 1 to n
        # since we're incrementing by n, we don't change the value (we're using mod n)
        for i in range(n):
            # the presence of a certain number in the array is stored in the array itself 
            # changes the index of the array that's the same number as the value nums[i]
            x = nums[i] % n
            nums[x] += n
            
        # if we never incremented a nums array value, the integer division by n would be 0 (rounded down) 
        # this is because we changed any value greater than the length of the array to 0
        for i in range(n):
            if (nums[i] // n == 0):
                # we return the smallest particular index that hasn't been incremented (or isn't in the array)
                # i is the index of the first value we never added n to in the array
                return i 
              
        # if all other indices are present, the largest number, or the number 1 greater than the original array's length, is missing
        # this is just n since we had appended 0 at the beginning (the original array has length n - 1)
        return n
