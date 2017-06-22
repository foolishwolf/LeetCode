class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aR = int(a.split('+')[0])
        aI = int(a.split('+')[1].replace('i', ''))
        bR = int(b.split('+')[0])
        bI = int(b.split('+')[1].replace('i', ''))
        r = aR * bR - aI * bI
        i = aR * bI + aI * bR
        return str(r) + '+' + str(i) + 'i'