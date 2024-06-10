# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 백트래킹 
        answer_set = set([i for i in range(1, 10)])
        
        def backtracking(x, y): # 현재 좌표 
            temp_set = set()
            for i in range(9):
                
                if arr[i][x]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    backtracking(0, 0)    