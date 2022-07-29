# Problem: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
from collections import defaultdict

class Solution(object):
    # With Iteration : O(n^2) time and O(n) space solution
    def singleNumberSol1(self, nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
    # With Hash Table : O(n) time and O(n) space 
     def singleNumberSOl2(self, nums : List[int]) -> int:
            hash_table = defaultdict(int)
            for i in nums:
                hash_table[i] += 1
             for i in hash_table:
                if hash_table[i] == 1:
                    return i
     # Arithmetic Wizadry : We will use the "set" operation in python to reduce nums to
     # the set of unique numbers within nums, which should take O(n) space 
     # the sum function will also take O(n) time as we iterate through set(nums) 
     def singleNumberSol3(self, nums): 
        return 2 * sum(set(nums)) - sum(nums)
     # Bit-manipulation solution : There is automatic type-conversion in python
     # a number XOR'ed with itself is equal to zero, only the unique number will remain
     def singleNumberSol4(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a 
        
