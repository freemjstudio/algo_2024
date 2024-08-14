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
                x, y = int(x), int(y)
                dots.append((x, y))
    min_x = min(dot[0] for dot in dots)
    max_x = max(dot[0] for dot in dots)
    min_y = min(dot[1] for dot in dots)
    max_y = max(dot[1] for dot in dots)

    # 교점을 배열에 그리기
    if len(dots) == 1: 
        return ["*"]
    answer = []
    for y in range(max_y, min_y-1, -1):
        row = ""
        for x in range(min_x, max_x+1):
            if (x, y) in dots: 
                row += "*"
            else: 
                row += "."
        answer.append(row)
    return answer 

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