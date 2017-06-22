class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        batCnt = 0
        height = len(board)
        width = len(board[0])
        for row in range(height):
            for col in range(width):
                if board[row][col] == 'X':
                    if row > 0 and board[row-1][col] == 'X' \
                    or col > 0 and board[row][col-1] == 'X':
                        continue
                    else:
                        batCnt += 1
        return batCnt