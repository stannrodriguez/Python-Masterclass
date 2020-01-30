"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
    	from collections import deque
    	count = maxCount = 0
    	d = {}
    	q = deque()
    	for i, val in enumerate(s):

    		if val not in q:
    			count += 1
    			d[val] = i
    			q.append(val)
    			maxCount = max(count, maxCount)
    			if val == '!':
    				print(' I was here')
    				print(count, maxCount)
    		else:
    			start = d[val] 
    			count = i - start
    			d[val] = i
    			q.append(val)
    			while q[0] != val:
    				q.popleft()
    		print(maxCount, val, q, d)
    	return maxCount

    def lengthofLongestSubstring2(self, s:str) -> int:
    	"""Cleaner code from stackoverflow"""
    	left_most_valid = 0
        longest = 0
        last_seen = {}

        for i, letter in enumerate(s):
            if letter in last_seen:
                # left_most_valid must be greater than any position which has been seen again
                left_most_valid = max(left_most_valid, last_seen[letter] + 1)
            last_seen[letter] = i

            # Length of substring from left_most_valid to i is i - left_most_valid + 1
            longest = max(longest, i - left_most_valid + 1)

        return longest

print(Solution().lengthOfLongestSubstring1('abcabcbb'))
print(Solution().lengthOfLongestSubstring1('bbbbb'))
print(Solution().lengthOfLongestSubstring1('pwwkew'))
print(Solution().lengthOfLongestSubstring1('dvdf'))
print(Solution().lengthOfLongestSubstring1('tmmzuxt'))
print(Solution().lengthOfLongestSubstring1('aabaab!bb'))

       