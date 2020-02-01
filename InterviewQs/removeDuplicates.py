class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # iterate through array
        # Track: value, index, replaceIndex
        
        i = 0
        replaceIndex = 0
        uniqueCount = 0
        for value in nums:
            if i == 0:
                uniqueCount += 1
                replaceIndex += 1
            elif value != nums[i-1]: # unique
                # replace repeated number slot
                nums[replaceIndex] = value
                # both unique
                uniqueCount+=1
                replaceIndex+=1
                
            i += 1
        return uniqueCount
                
        