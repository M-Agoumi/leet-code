from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line = {}
        column = {}
        box = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if (i, board[i][j]) in line or (j, board[i][j]) in column or (i//3, j//3, board[i][j]) in box:
                        return False
                    line[(i, board[i][j])] = 1
                    column[(j, board[i][j])] = 1
                    box[(i//3, j//3, board[i][j])] = 1
        
        return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))