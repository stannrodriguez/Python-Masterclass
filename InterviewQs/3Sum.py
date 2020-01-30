class Solution:
    def threeSum(self, nums):
        from itertools import combinations

        answer = []
        for x,y in list(combinations(nums,2)):
        	z = 0 - x - y
        	if z in nums:
        		triplet = [x,y,z]
        		triplet.sort()
        		if triplet not in answer:
        			answer.append(triplet)

        return answer

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))