# https://www.acmicpc.net/problem/2531
N, d, k, c = map(int, input().split())
answer = 0
arr = []

for _ in range(N):
    arr.append(int(input()))
sushi = arr + arr

for i in range(N):
    dish = sushi[i:i+k]
    dish.append(c)
    answer = max(answer, len(set(dish)))
print(answer)