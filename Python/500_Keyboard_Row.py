class Solution(object):

    def __init__(self):
        self.alp = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []
        for srcWord in words:
            word = srcWord.lower()
            for alp in self.alp:
                isInRow = False
                if word[0] in alp:  
                    for letter in word:
                        print letter
                        if letter in alp:
                            isInRow = True
                        else:
                            isInRow = False
                            break
                    print alp
                if isInRow:
                    ret.append(srcWord)
                    break
        return ret

sol = Solution()
print sol.findWords(["Hello","Alaska","Dad","Peace"])