"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

# Strategy
# Data structure of choice: List s
# Go through list
# - If character is }, ), ] and len(s) == 0: return False
# - If character is (, {, [: append to s
# - If character closes off previous character, pop it off stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
        	return True

        stack = []
        pairs = {'}':'{', ')':'(', ']':'['}
        for character in s:
        	if character in pairs.keys() and len(stack) == 0:
        		return False
        	elif character in pairs.values():
        		stack.append(character)
        	elif len(stack) > 0:
        		if pairs[character] == stack[-1]:
        			stack.pop()
        		else:
        			return False

        if len(stack) == 0:
        	return True
        else:
        	return False

print(Solution().isValid('()'))
print(Solution().isValid('([{}])'))
print(Solution().isValid('([)]'))
print(Solution().isValid('(])'))