# https://school.programmers.co.kr/learn/courses/30/lessons/87377

from itertools import combinations 

def print_arr(arr):
    for a in arr: 
        print(*a)

def solution(line):
    dots = [] # 교점 
    comb = list(combinations(line, 2))
    for items in comb:
        l1, l2 = items # line1, line2 
        a, b, e = l1
        c, d, f = l2 
        # 두 직선 간 교점이 없는 경우 AD - BC = 0
        if a*d == b*c:
            continue
        else: # 교점이 있는 경우 
            x = (b*f - e*d)/(a*d - b*c)
            y = (e*c - a*f)/(a*d - b*c) 
            # print(x, y)
            # 정수인지 확인 
            if int(x) == x and int(y) == y:
                dots.append((int(x), int(y)))

    print("DOTS", dots)
    # 교점을 배열에 그리기
    if len(dots) == 1: 
        return ["*"]
    min_x, min_y, max_x, max_y = int(1e9), int(1e9), -int(1e9), -int(1e9) 
    for x, y in dots: 
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)
    print(min_x, min_y, max_x, max_y)
    answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in dots:
        answer[y - min_y][x - min_x] = "*" # 이것도 왜 x,y 가 아니라 y,x 인지 모르겠음 
        print(y - min_y, x - min_x)
    answer.reverse() # 이걸 이해못함 
    return ["".join(row) for row in answer]

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
"""
["....*....", 
".........", 
".........", 
"*.......*", 
".........", 
".........", 
".........", 
".........", 
"*.......*"]
"""
print_arr(solution(line))

line2 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print_arr(solution(line2))