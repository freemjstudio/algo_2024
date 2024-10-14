# https://leetcode.com/problems/construct-quad-tree/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List 

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        # 정사각형 내부의 값이 모두 동일한지 확인 
        def check_sqaure(x, y, n):
            val = grid[x][y]
            for i in range(x, x+n):
                for j in range(y, y+n):
                    if grid[i][j] != val: 
                        return False 
            return True 
        
        
        # 동일하면 quad 로 카운트하기,
        # 동일하지 않으면 정사각형을 4개로 나눔 -> 다시 check_square 호출 
        def make_quad_tree(n):
            l = 
            up_left = check_sqaure()
            up_right = check_sqaure() 
            down_left =check_sqaure() 
            down_right = check_sqaure()
            
        make_quad_tree(n)
        return 
    
s = Solution()
grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
print(s.construct(grid))

