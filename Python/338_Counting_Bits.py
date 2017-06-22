class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        repeatNum = 1
        bitNumList = [0] * (num + 1)
        if num == 0:
            return bitNumList
        for i in range(1, num + 1):
            print repeatNum
            bitNumList[i] = bitNumList[i-repeatNum] + 1
            if (i + 1) % repeatNum == 0:
                repeatNum *= 2
        return bitNumList