class Solution:
    """
    Class for the solution to LeetCode Problem 41: First Missing Positive
    """

    def first_missing_positive(self, nums: list[int]) -> int:
        """
        Finds and returns the smallest missing positive integer in nums

        :param nums: Unsorted integer array
        :return: smallest missing positive integer in nums
        """
        # change all elements that are out of the possible range of values to 0
        length = len(nums)
        for idx in range(length):
            if nums[idx] < 1 or nums[idx] > length:
                nums[idx] = 0

        # append 0 to account for the possibility that all values in nums are the smallest possible positive integers, meaning we need to go above those
        nums.append(0)
        length += 1

        # helper variable to make it easier to know when to move pointer
        already_incremented = False
        # idx will be used when updated certain elements
        # pointer will be the starting element to update
        idx = pointer = 0
        while pointer < length:
            # if the current element is -1, it has already been updated, so move pointer if possible else return the answer
            if nums[pointer] == -1:
                if pointer + 1 < length:
                    pointer += 1
                    continue
                else:
                    return self.check_smallest(nums)
            temp = pointer
            # if the current element is not 0, we use the element at temp as our next index
            # otherwise, we don't need to use temp, so move pointer if possible else return the answer
            if nums[temp] != 0:
                idx = nums[temp] - 1
            else:
                if pointer + 1 < length:
                    pointer += 1
                    continue
                else:
                    return self.check_smallest(nums)

            # while we do not arrive at an element that has already been updated
            while nums[idx] != -1:
                # if we arrive at an element that is 0, update the element to -1
                # then, move pointer if possible else return the answer
                if nums[idx] == 0:
                    nums[idx] = -1
                    if pointer + 1 < length:
                        already_incremented = True
                        pointer += 1
                        break
                    else:
                        return self.check_smallest(nums)
                # if we arrive at an element that is -1, it has already been updated
                # so, move pointer if possible else return the answer
                elif nums[idx] == -1:
                    if pointer + 1 < length:
                        already_incremented = True
                        pointer += 1
                        break
                    else:
                        return self.check_smallest(nums)
                # otherwise, store the current element in temp, update the element, and set the new index to the value of temp
                else:
                    temp = nums[idx] - 1
                    nums[idx] = -1
                    idx = temp

            # if the previous while loop was immediately exited, then move pointer if possible else return the answer
            if nums[idx] == -1 and not already_incremented:
                if pointer + 1 < length:
                    pointer += 1
                else:
                    return self.check_smallest(nums)
            already_incremented = False

    def check_smallest(self, nums: list[int]) -> int:
        """
        Helper function that traverses nums to find the smallest missing positive integer

        :param nums: Unsorted integer array
        :return: smallest missing positive integer in nums
        """
        for idx in range(len(nums)):
            # if an element is not -1, then that element has not been updated
            # therefore, that element's 1-based index is the smallest missing positive integer and is returned
            if nums[idx] != -1:
                return idx + 1
