############################  TWO SUM ########################
#
# Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one
# solution, and you may not use the same element twice.
#
# You can return the answer in any order.


class Solution_On2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leng = len(nums)

        # Naive, screen through all elements

        for i in range(0, leng):
            for j in range(i + 1, leng):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


class Solution_On_hashmap(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create hasmap to save elements
        #  of array as keys, so has to travese
        #  array only once

        seen = {}

        for i, num in enumerate(nums):
            supplement = target - num
            # get supplement and search if has been found
            if supplement in seen:  # check if already a key
                return [seen[supplement], i]
            # keep in seen
            seen[num] = i

        # In the dictionary, the key is actually
        # an element of the array nums, while
        # the value is its index. This is done because
        # if in checks for keys and not values.
