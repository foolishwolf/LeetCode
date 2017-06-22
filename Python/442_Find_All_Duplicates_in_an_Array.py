class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dupList = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                dupList.append(abs(num))
            nums[abs(num)-1] = -nums[abs(num)-1]
        return dupList