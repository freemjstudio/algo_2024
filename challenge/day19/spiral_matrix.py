# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        
        # 우, 하, 좌, 상 
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        n = len(matrix)
        m = len(matrix[0])
        visited = [[False] * m for _ in range(n)]
        d = 0 # 방향키 

        x, y = 0, 0 
        
        for i in range(n*m):
            answer.append(matrix[x][y])
            visited[x][y] = True 
            x, y = x + dx[d], y + dy[d]
            if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] == True:
                x, y = x - dx[d], y - dy[d]
                d = (d+1) % 4
                x, y = x + dx[d], y + dy[d]
        
        return answer 

t = [[1,2,3]
     ,[4,5,6]
     ,[7,8,9]]
s = Solution()
print(s.spiralOrder(t))