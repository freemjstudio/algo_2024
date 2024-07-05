# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        
        # 우, 하, 좌, 상 
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        n = len(matrix)
        m = len(matrix[0])
        visited = [[False] * m for _ in range(n)]
        total = n*m # matrix 칸의 개수 
        count = 0 
        dir = 0 # 방향키 

        x, y = 0, 0 
        for i in range(n*m):
            
            if visited[x][y] == True or not (0 <= x < n) or not (0 <= y > m):
                # 방향 회전하기 
                dir = (dir+1) % 4
            visited[x][y] = True 
            x, y = x + dx[dir], y + dy[dir]
            
        
        return answer 
        