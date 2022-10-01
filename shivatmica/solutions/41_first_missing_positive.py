class Problem41:
    """
    Class for First Missing Positive (#41)
    https://leetcode.com/problems/first-missing-positive/
    """
    def first_missing_positive(self, 
                               nums: List[int]
                              ) -> int:
        """
        Returns the smallest positive number that isn't included in the inputted list
        For each of the elements of the array nums_c, a copy of the nums array, we begin by removing any elements that are negative 
        or greater than n (the length of the array) since we don't need to consider these (the list only should ultimately include 
        values from 1 to n). We iterate through the array nums_c and for each element, if the value of the element is k, we add n 
        to the number at index k. Once we've updated each of the values, we iterate through the updated array once again and consider
        the integer quotient (nums_c[i]/n), which represents the number of times we added n to the number at that particular index. For 
        example, if we want to know how many times the number k was included in the original array, we consider the number x at 
        the index k in the array and the integer quotient x/n tells us the number of times the element k was included in the list
        nums. The first index i where the quotient is 0 means that the number i was never included in the list and we return i. 
        If all the numbers from 1 to n are included in the array, we return n + 1 since that's the first positive number not 
        included in the list nums.
        
        Time complexity: O(n) [where n is the length of nums_c]
        Space complexity: O(n) [where n is the length of nums_c]
        
        :param nums: the inputted list, an unsorted integer array
        :return: the index of the first missing positive number
        """
        
        # adding 0 to the end of the list in the case that all the numbers are consecutive and smallest positive numbers
        # the function will then return the value that is greater than all of these values
        nums_c = nums.copy()
        nums_c.append(0) 
        n = len(nums_c)
        
        # we can change any irrelevant values that are greater than n or negative to be 0 so they aren't checked 
        for i in range(n):
            if nums_c[i] < 0 or nums_c[i] >= n:
                nums_c[i] = 0
        
        # updates index i about the value i in the range from 1 to n
        # since we're incrementing by n, we don't change the value (we're using mod n)
        for i in range(n):
            # the presence of a certain number in the array is stored in the array itself 
            # changes the index of the array that's the same number as the value nums_c[i]
            x = nums_c[i] % n
            nums_c[x] += n
            
        # if we never incremented a nums array value, the integer division by n would be 0 (rounded down) 
        # this is because we changed any value greater than the length of the array to 0
        for i in range(n):
            if (nums_c[i] // n == 0):
                # we return the smallest particular index that hasn't been incremented (or isn't in the array)
                # i is the index of the first value we never added n to in the array
                return i 
              
        # if all other indices are present, the largest number, or the number 1 greater than the original array's length, is missing
        # this is just n since we had appended 0 at the beginning (the original array has length n - 1)
        return n
