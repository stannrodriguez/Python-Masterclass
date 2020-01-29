# Leetcode: Hard

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

### First Solution
# Runtime: faster than 16.51% of all Python3 submissions
# Memory Usage: less than 100% of all Python3 submissions

def findMedianSortedArrays(nums1, nums2):
    l = len(nums1)+len(nums2)
    q, r = divmod(l, 2)
    
    nums = nums1 + nums2
    nums.sort()
    
    if r == 1:
        return nums[q]
    else:
        return sum(nums[q-1:q+1])/2

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))

### Solution in Logarithmic time
# Read: https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
