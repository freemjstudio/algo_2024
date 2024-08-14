# https://school.programmers.co.kr/learn/courses/30/lessons/87377

from itertools import combinations 
def solution(line):
    answer = []

    comb = list(combinations(line, 2))
    for items in comb:
        l1, l2 = items # line1, line2 
        # AD - BC = 0 
        if 


    return answer

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
solution(line)


line2 = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(line2))