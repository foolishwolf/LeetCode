import math

class Solution(object):
    # def hammingDistance(self, x, y):
    #     """
    #     :type x: int
    #     :type y: int
    #     :rtype: int
    #     """
    #     restX = x
    #     restY = y
    #     x2 = []
    #     y2 = []
    #     dist = 0
    #     while restX not in [0,1]:
    #         x2.append(restX % 2)
    #         restX = int(math.floor(restX / 2))
    #     x2.append(restX)
    #     while restY not in [0,1]:
    #         y2.append(restY % 2)
    #         restY = int(math.floor(restY / 2))
    #     y2.append(restY)
    #     for i in range(0, max(len(x2), len(y2))):
    #         if i < len(x2) and i < len(y2):
    #             dist += x2[i] ^ y2[i]
    #         elif i < len(x2):
    #             dist += x2[i]
    #         elif i < len(y2):
    #             dist += y2[i]
    #     return dist

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x).replace('0b','')
        y = bin(y).replace('0b','')
        x = '0' * (max(len(x), len(y))-len(x)) + x
        y = '0' * (max(len(x), len(y))-len(y)) + y
        dist = 0
        for i in range(0, len(x)):
            dist += int(x[i]) ^ int(y[i])
        return dist

        

sol = Solution()
print sol.hammingDistance(1, 4)