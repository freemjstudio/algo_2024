# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        # 1 - 9 사이의 숫자들 
        numbers = [str(i) for i in range(1, 10)]
        
        # 이미 등장한 숫자이면 false 
        def check_valid(row:int, col:int, target:str) -> bool:
            for i in range(9):
                if board[i][col] == target or board[row][i] == target or board[(row//3) * 3 + (i//3)][(col//3)*3 + (i%3)] == target:
                    return False 
            return True 
        
        def solve(count: int) -> bool:
            if count == 81: # 모든 숫자를 채움 
                return True 
            
            i, j = count // 9, count%9 
            
            # 이미 숫자로 채워져 있는 칸은 pass 
            if board[i][j] != ".":
                return solve(count+1)
            
            for n in numbers:
                if check_valid(i, j, n):
                    board[i][j] = n 
                    if solve(count+1):
                        return True 
                    board[i][j] = "."
            
            return False 
        
        solve(0)