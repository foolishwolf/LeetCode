class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sister = set([])
        cnt = 0
        for candy in candies:
            if candy not in sister:
                cnt += 1
                if cnt > len(candies)/2:
                    return len(candies)/2
                sister.add(candy)
        return len(sister)