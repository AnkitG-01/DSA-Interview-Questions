import numpy as np
class Solution:
    def possible(self, board, x, y, n):
        for i in range(9):
            if board[x][i]==n:
                return False
        for i in range(9):
            if board[i][y]==n:
                return False
        xs=(x//3)*3
        ys=(y//3)*3
        for i in range(3):
            for j in range(3):
                if board[xs+i][ys+j]==n:
                    return False
        return True
    def solveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for n in range(1,10):
                        if self.possible(board,i,j,chr(n+ord("0"))):
                            board[i][j]=chr(n+ord("0"))
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]='.'
                    return False
        return True

s=Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(np.matrix(board))