"""

https://leetcode.com/problems/snakes-and-ladders/?envType=study-plan-v2&envId=top-interview-150

You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)]. -> backtracking 으로 횟수를 세어야 할 것 같다. 모든 경우의 수의 ! 
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations,

regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. 
The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

Input: board = 
[[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]

Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1
"""

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_curr_pos(curr):
            x = (curr-1) // n 
            y = (curr-1) % n # 짝수 
            if x%2 == 1: # 홀수 row 인 경우 
                y = n - y -1
            return n - x -1, y

        dice_count = 0 # dice counter
        queue = deque([1]) # 시작하는 칸 : 1
        visited = {1} # 방문한 칸 기록

        while queue:
            for _ in range(len(queue)):
                curr_pos = queue.popleft()

                if curr_pos == n*n:
                    return dice_count
                
                for next_pos in range(curr_pos + 1, min(curr_pos + 6, n*n)+1):
                    x, y = get_curr_pos(next_pos)

                    if board[x][y] != -1:
                        next_pos = board[x][y]
                    
                    if next_pos not in visited: 
                        queue.append(next_pos)
                        visited.add(next_pos)
            dice_count += 1

        return -1 