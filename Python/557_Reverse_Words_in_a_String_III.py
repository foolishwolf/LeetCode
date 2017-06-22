class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split(' ')
        reStr = ''
        for word in sList:
            reStr += word[::-1] + ' '
        return reStr.strip()