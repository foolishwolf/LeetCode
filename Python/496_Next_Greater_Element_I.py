class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ngMap = {}
        ngStack = []
        ret = []
        for num in nums:
            while ngStack != [] and num > ngStack[-1]:
                ngMap[ngStack.pop()] = num
            ngStack.append(num)
        
        for num in findNums:
            if num in ngMap:
                ret.append(ngMap[num])
            else:
                ret.append(-1)
        
        return ret