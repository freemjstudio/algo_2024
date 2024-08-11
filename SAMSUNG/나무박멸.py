# https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/description?page=1&pageSize=20&name=%EB%82%98%EB%AC%B4

n, m, k, c = map(int, input().split())

answer = 0 # m 년 동안 총 박멸할 나무 그루 수 
arr = []
killer_arr = [] # 제초제 위치와 남은 년수 기록하기, 벽의 위치 정보는 필요함

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 대각선 탐색
dx2 = [-1, 1, -1, 1]
dy2 = [-1, -1, 1, 1]

def growth():
    grow_pos = [] # 성장이 일어날 위치 기록

    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0: # 나무가 있으면 상하좌우 탐색하기
                # 인접한 네 개의 칸 중 나무가 있는 칸의 수 카운트
                cnt = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                        cnt += 1
                if cnt > 0:
                    grow_pos.append((x, y, cnt))
    # update arr
    for x, y, amount in grow_pos:
        arr[x][y] += amount


for _ in range(m):
    growth()