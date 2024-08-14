# https://school.programmers.co.kr/learn/courses/30/lessons/87377

from itertools import combinations 

def print_arr(arr):
    for a in arr: 
        print(*a)

def solution(line):
    answer = [] # 출력할 답 
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
    
    return answer

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print_arr(solution(line))


line2 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print_arr(solution(line2))