class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums[0]) == 0:
            return nums
        if len(nums) * len(nums[0]) != r * c:
            return nums
        rCnt = 0
        cCnt = 0
        reRowList = []
        reMatList = []
        for row in range(0, len(nums)):
            for col in range(0, len(nums[row])):
                if cCnt < c:
                    reRowList.append(nums[row][col])
                    cCnt += 1
                if cCnt == c:
                    reMatList.append(reRowList)
                    reRowList = []
                    cCnt = 0
                    rCnt += 1
        return reMatList
