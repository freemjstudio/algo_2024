#  https://www.codetree.ai/training-field/frequent-problems/problems/ancient-ruin-exploration/description?page=1&pageSize=20

from collections import deque 

k, m = map(int, input().split())
answer = []
arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))

wall_numbers = list(map(int, input().split())) # m 개 
wall_idx = 0 # 벽면 숫자 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
blank = [] # 빈칸 

# 중점 
for i in range(1, 4):
    for j in range(1, 4):
        

# (x, y) -> (y, n - x + 1)
def rorate_box(i, j): # 시계 방향 90, 180, 270
    for rorate in range(4):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                arr[y][3 - x + 1] = arr[x][y]
        if rorate == 3: 
            return # 함수 종료 
        # 유물 획득 시작하기 
     

def get_germ(): # 유물 획득 - bfs
    queue = deque([])
    queue.    

def fill_with_new_block(): # 새롭게 채우기 

# 유물 연쇄 획득 

# K 번 반복 