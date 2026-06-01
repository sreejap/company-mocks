# https://leetcode.com/problems/battleships-in-a-board/
# it is sufficient to count the start point, we don't need full dfs here - https://algo.monster/liteproblems/419
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # do a dfs of the board and use connected components 
        if not board:
            return 0

        bships = 0
        m = len (board)
        n = len (board[0])

        # if it is hard to make the if / else , flip the conditions to make it simpler
        for i in range (m):
            for j in range (n):
                if board [i][j] == '.':
                    continue

                if i > 0 and board [i-1][j] == 'X':
                    continue
                if j > 0 and board [i][j-1] == 'X':
                    continue
                bships += 1                 
        return bships
