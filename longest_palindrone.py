###########  LONGEST PALINDROMIC SUBSTRING ####################

# Given a string s, return the longest palindromic substring in s.

class Solution_on2_naive(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Edge cases:
        #   - string can be single character:

        palindromes = []

        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    palindromes.append(s[i:j])

        return max(palindromes, key = len)

class Solution_On3_worst(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Edge cases:
        #   - string can be single character:

        # Alternative solution, go through all center digits and check if
        # the digit before or after is the same. If yes, expand around this
        # substrict checking for palindrome until failure --> will not consider
        # even-length palindromes

        # Take each digit, check if adding left or right digit can make palindrome
        # if not, stop searching and move the next, if yes, continue.

        max_length = 1
        max_pal = ""

        for i in range(0, len(s) - 1):
            # It will only be part of palindrome if next digit is the same, or if
            # the next next one is the same
            if s[i] == s[i + 1]:
                # Even palindrome found, can we expand it, i - 1 elements to the left
                # of i and len(s) - (i+1) elements to the right of i + 1
                if i > 0 and  len(s) - (i + 2) > 0 :
                    for j in range(1, min(i + 1, len(s) - i - 1)):
                        if s[i-j : i+2+j] == s[i-j : i+2+j][::-1]:
                            if len(s[i-j : i+2+j]) > max_length:
                                max_pal = s[i-j : i+2+j]
                                max_length = len(max_pal)
                        else:
                            if len(s[i-j+1 : i+1+j]) > max_length:
                                max_pal = s[i-j+1 : i+1+j]
                                max_length = len(max_pal)
                            break
                else:
                    if len(s[i:i+2]) > max_length:
                        max_pal = s[i:i+2]
                        max_length = len(max_pal)

            #i = 5
            if i < len(s) - 2 and s[i] == s[i + 2]:
                # Off palindrome found, can we expand it, i-1 elements to the left of
                # of i and len(s) - (i+2) elements to the right of i + 2
                if i > 0 and  len(s) - (i + 3) > 0 :
                    for j in range(1, min(i + 1, len(s) - (i + 2))):
                        if s[i-j : i+3+j] == s[i-j : i+3+j][::-1]:
                            if len(s[i-j : i+3+j]) > max_length:
                                max_pal = s[i-j : i+3+j]
                                max_length = len(max_pal)
                        else:
                            if len(s[i-j+1 : i+2+j]) > max_length:
                                max_pal = s[i-j+1 : i+2+j]
                                max_length = len(max_pal)
                            break
                else:
                    if len(s[i:i+3]) > max_length:
                        max_pal = s[i:i+3]
                        max_length = len(max_pal)

        if max_length == 1:
            return s[0]
        else:
            return max_pal

class Solution_optimal(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Edge cases:
        #   - string can be single character: OK

        if len(s) == 1:
            return s

        # first, to differentiate odd and even palindromes,
        # add # in between every character -> all strings will
        # become odd: 2n + 2n + 1 is odd and 2n + 1 + 2n + 2 is
        # also odd.

        s = "#" + "#".join(s) + "#"

        # initializing needed variables
        dp = [0] * len(s)   # the radius of the palindrome sitting at i
        center = 0          # tracking center of deepest/rightmost palidrome found
        radius = 0           # tracking radius of right-most found palindrome

        # current maximum length and string
        max_str = s[0]
        max_len = 0 #want to be able to find strign of length 1

        for i in range(len(s)):

            # now, if we are within the bounds of an already found palindrome,
            # we can reuse it so we don't have to expand below again using the
            # iterative index j, so we take the radius at the symmetric site
            # with respect to center.

            if i < center + radius:
                # we need to make sure the symmetric side is not outside of bounds
                # of the currently found palindrome.
                dp[i] =  min(dp[center - (i - center)], center + radius - i)

            #check for palindrome, and keep doing so within bounds
            # create iterative index, and if dp[i] has been resued, we start with it
            j = dp[i]
            while i - j >= 1 and i + j + 1 < len(s):
                if s[i-1-j] == s[i+1+j]: #palindrome found centered at i
                    dp[i] += 1
                else:
                    break
                j += 1


            # if found palindrome is above the known boundary, will be used later
            if i + dp[i] > center + radius:
                center = i
                radius = dp[i]

            # if found palindrome is larger
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i-dp[i] : i+1+dp[i]].replace("#", "")

        return max_str
