class Solution:
    def countBattleships(self, board):
        acc = 0
        def iter(i, j):
            if i < len(board) and j < len(board[0]):
                if board[i][j] == 'X':
                    board[i][j] = '.'
                    iter(i + 1, j)
                    iter(i, j + 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    iter(i, j)
                    acc += 1
        
        return acc

print(Solution().countBattleships([
    ['X', '.', 'X'],
    ['.', 'X', 'X'],
    ['.', '.', 'X'],
]))