###########  LONGEST SUBTRING W/O REPEAT CHAR ####################

# Given a string s, find the length of the longest
#  substring without duplicate characters.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #Edge cases:
        #   - string can have 0 length: OK
        #   - string can contain spaces, symbols, etc: OK
        #   - no repeats in array: OK


        # Create dictionary for characters seen
        
        seen = {}
        start = 0
        max_len = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                # Found duplicate within current window, move start
                start = seen[char] + 1
            seen[char] = i
            max_len = max(max_len, i - start + 1)

        return max_len
