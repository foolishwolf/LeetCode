class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxProd = [0]*len(nums)
        minProd = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                maxProd[i] = nums[i]
                minProd[i] = nums[i]
            else:
                maxProd[i] = max(max(nums[i] * maxProd[i-1], nums[i] * minProd[i-1]), nums[i])
                minProd[i] = min(min(nums[i] * maxProd[i-1], nums[i] * minProd[i-1]), nums[i])
        return max(maxProd)