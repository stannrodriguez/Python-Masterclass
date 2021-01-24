"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [];
        remove_stack = [];

        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    remove_stack.append(index)
            else:
                continue

        remove_indices = stack + remove_stack
        return "".join([char for index, char in enumerate(s) if index not in remove_indices])

print(Solution().isValid('lee(t(c)o)de)'))
print(Solution().isValid('a)b(c)d'))
print(Solution().isValid('))(('))
print(Solution().isValid('(a(b(c)d)'))