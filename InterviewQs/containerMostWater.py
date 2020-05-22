"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

# Brute Force Solution
class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curr_max = 0
        for index1, h1 in enumerate(height):
        	for index2, h2 in enumerate(height):
        		curr_area = min(h1, h2) * abs(index1 - index2)
        		if curr_area > curr_max:
        			curr_max = curr_area

        return curr_max
        
print(Solution1().maxArea([1,8,6,2,5,4,8,3,7]))    

# Brute Force Solution
class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h, i = 0, 0
        left_corners = []
        for pt in height:
        	if pt > h:
        		left_corners.append((pt,i))
        		h = pt
        	i += 1

        h, i = 0, len(height) - 1
        right_corners = []
        for pt in height[::-1]:
        	if pt > h:
        		right_corners.append((pt,i))
        		h = pt
        	i -= 1

        area = 0
        for L in left_corners:
        	for R in right_corners:
        		if L[0] < R[0]:
        			area = max(L[0] * abs(L[1]-R[1]), area)
        		else:
        			area = max(R[0] * abs(L[1]-R[1]), area)

        return area
        
print(Solution2().maxArea([1,8,6,2,5,4,8,3,7]))    

