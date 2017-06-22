class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        capitalCnt = 0
        for letter in word:
            if letter <= 'Z':
                capitalCnt += 1
        if capitalCnt == len(word) or capitalCnt == 0 or capitalCnt == 1 and word[0] <= 'Z':
            return True
        else:
            return False