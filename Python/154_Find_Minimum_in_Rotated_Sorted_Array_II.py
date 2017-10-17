class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = nums[0]
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                minNum = nums[i]
        return minNum
        