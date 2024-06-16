class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        numbers = [str(i) for i in range(1, 10)]
        
        def is_valid(row, col, num):
            for k in range(9):
                if board[row][k] == num and k != col:
                    return False 
                if board[k][col] == num and k != row:
                    return False 
                nr, nc = 3*(row//3) + k//3, 3*(col//3) + k%3
                if board[nr][nc] == num and not (nr == row and nc == col):
                    return False 
            return True 
                
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue 
                if not is_valid(i, j, board[i][j]):
                    return False 
        return True 
        