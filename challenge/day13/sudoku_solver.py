# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 백트래킹 
        answer_set = set([i for i in range(1, 10)])
        
        def check_valid():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return False 
            return True 
        
        def backtracking(x, y): # 현재 좌표 
            
            temp_set = set()
            if check_valid():
                return # 재귀 함수 탈출 
            for i in range(9):
                for j in range(9):
                    if arr[i][x] == '':
                    
        
        # 함수 실행 
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    backtracking(i, j)    