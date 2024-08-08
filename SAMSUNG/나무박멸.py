# https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/description?page=1&pageSize=20&name=%EB%82%98%EB%AC%B4

n, m, k, c = map(int, input().split())

answer = 0 # m 년 동안 총 박멸할 나무 그루 수 
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

