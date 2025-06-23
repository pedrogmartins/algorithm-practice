###########  LONGEST CONSECUTIVE SEQUENCE ####################

# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

class Solution_attempt1(object):

    # Proposed solution does not take into
    #  account that there might be mulitple
    #  regions with consecutive numbers, only
    #  need largest one

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = [9,1,4,7,3,-1,0,5,8,-1,6]
        # Remove all duplicates and order entries
        sorts = sorted(list(set(nums)))
        seq = []
        print(sorts)

        if len(sorts) == 1:
            return 1

        for i, num in enumerate(sorts):

            if i < len(sorts) - 1 and (num + 1) == sorts[i+1]:
                # Append both the value and its next
                seq.append(num)
                seq.append(sorts[i+1])

        # Only unique values should count in length
        return len(list(set(seq)))


class Solution_nlogn(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Edge cases:
        #   - array can be empty or single-valued: OK
        #   - array elements can be negative: OK

        # Remove all duplicates and order entries
        sorts = sorted(list(set(nums)))

        if len(sorts) < 2:
            return len(sorts)

        current_slice = [sorts[0]]
        slices_len = []

        #Go through array and split where the condition is not met
        for i in range(1, len(sorts)):

            if sorts[i] == sorts[i-1] + 1:
                # Next element is part of sequence, add to slice
                current_slice.append(sorts[i])
                # print(current_slice)

            else:
                # Next element is not in sequence, start new slice
                # and compile previous slice's len
                slices_len.append(len(current_slice))
                #Restart next array with current element
                current_slice = [sorts[i]]

            if i == len(sorts) - 1:
                # If entire array is a sequence, make sure to add
                # to list of slices
                slices_len.append(len(current_slice))

        return max(slices_len) #Will fail if array is empty



class Solution_On_set(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Edge cases:
        #   - array can be empty or single-valued: OK
        #   - array elements can be negative: Ok

        if not nums:
            return 0

        # Create set fot quicker in check
        nums_set = set(nums)
        longest = 0

        for num in nums_set:

            if num - 1 not in nums_set:
                currrent = num
                streak = 1

                while currrent + 1 in nums_set:
                    currrent += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
