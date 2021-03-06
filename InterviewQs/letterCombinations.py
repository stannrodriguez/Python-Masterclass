"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
        }

        i = 0
        for digit in digits:
        	new_combos = []
        	if i == 0:
        		old_combos = mapping[int(digit)]
        		new_combos = old_combos
        	else:
        		for letter in mapping[int(digit)]:
        			new_combos += [combo+letter for combo in old_combos]
        		old_combos = new_combos
        	i += 1
        	
        return new_combos

print(Solution().letterCombinations('2'))
