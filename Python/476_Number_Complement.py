class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        for i in range(33):
            if num < 2**i:
                return 2**i -1 - num