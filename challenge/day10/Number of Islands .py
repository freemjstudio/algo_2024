# https://leetcode.com/problems/number-of-islands/

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0 
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(sx, sy):

            queue = deque([])
            queue.append((sx, sy))
            
            while queue:
                x, y = queue.popleft() 
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == "1":
                        visited[nx][ny] = True 
                        queue.append((nx, ny))
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    answer += 1
 
                        
        return answer 
                    
                