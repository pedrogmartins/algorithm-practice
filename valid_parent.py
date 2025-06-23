#######################  VALID PARENTHESIS #######################

# Given a string s containing just the characters '(', ')', '{', '}',
#    '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution_On2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        opn = ["(", "[", "{"]
        cld = [")", "]", "}"]
        stack = []

        # solution must have even number of entries
        if len(s) % 2 != 0:
            return False

        #trimmed = s

        for i in range(0, len(s)):
            if s[i] in opn:
                stack.append(s[i])
            elif s[i] in cld and stack != [] and cld.index(s[i]) == opn.index(stack[-1]):
                #Clean stack (very costly, creating new list in python with length k is O(k))
                stack = stack[0:-1]
            else:
                return False

        return stack == []

class Solution_optimal(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []


        for el in s:
            # Check if starts with opening, and add to stack
            if el in '([{':
                stack.append(el)

            else:
                # Stop if either stack is empty or non-match
                if stack == [] or pairs[el] != stack[-1]:
                    return False
                stack.pop()

        # A correct expression should return empty stack
        return stack == []
