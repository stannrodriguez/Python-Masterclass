"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

# Breaking down the problem
# For example one:
# 3 Strings: s[i] goes to string 1 -> 2 -> 3 -> 2 -> 1 -> 2 -> 3 -> 2 -> 1 -> 2 -> 3
# For example two:
# 4 Strings: s[i] goes to string 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1  

# Data Structure of choice: dict
# dict[1] = string1, dict[2] = string2...
# at the end, return dict[1] + dict[2] + ....

# Brute force solution:
# Initialize answer string '', enumerate through s, append to strings 1-4 using pattern above, combine in the end
# Time complexity of brute force solution: O(n^2)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ''
        if len(s) == 1 or numRows == 1:
            return s

        answer = {}
        for i, letter in enumerate(s):
        	quotient, remainder = divmod(i, numRows-1)
        	if quotient % 2 == 0:
        		# Going down the list
        		answer[remainder] = answer.get(remainder, '') + letter
        	else:
        		# Going in the diagonal
        		answer[numRows-remainder-1] = answer.get(numRows - remainder -1, '') + letter

        convertedString = ''
        for string in answer.values():
        	convertedString += string
        
        return convertedString

print(Solution().convert('PAYPALISHIRING',3))
print(Solution().convert('PAYPALISHIRING',4))