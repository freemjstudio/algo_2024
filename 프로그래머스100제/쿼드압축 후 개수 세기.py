# https://school.programmers.co.kr/learn/courses/30/lessons/68936

"""
0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다. 당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 
구체적인 방식은 다음과 같습니다.

당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤,
각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
arr이 매개변수로 주어집니다. 
위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

제한사항
arr의 행의 개수는 1 이상 1024 이하이며, 2의 거듭 제곱수 형태를 하고 있습니다. 즉, arr의 행의 개수는 1, 2, 4, 8, ..., 1024 중 하나입니다.
arr의 각 행의 길이는 arr의 행의 개수와 같습니다. 즉, arr은 정사각형 배열입니다.
arr의 각 행에 있는 모든 값은 0 또는 1 입니다.

arr
[[1,1,0,0]
,[1,0,0,0]
,[1,0,0,1]
,[1,1,1,1]]

result 
[4,9]

arr
[[1,1,1,1,1,1,1,1]
,[0,1,1,1,1,1,1,1]
,[0,0,0,0,1,1,1,1]
,[0,1,0,0,1,1,1,1]
,[0,0,0,0,0,0,1,1]
,[0,0,0,0,0,0,0,1]
,[0,0,0,0,1,0,0,1]
,[0,0,0,0,1,1,1,1]]

result 
[10,15]
"""

def solution(arr):
    answer = [0, 0] #0 개수, 1 개수 
    n = len(arr)
    visited = [[False] * n for _ in range(n)]

    def check_visited(i, j, m):
        for i in range(i, i+m):
            for j in range(j, j+m):
                visited[i][j] = True

    def compress(x, y, l): # 좌측 상단 좌표 
        if visited[x][y]: # 이미 방문한적 있으면 처리하지 않음 
            return 
        if l == 1: # 1*1 칸의 경우 (더이상 재귀함수 호출이 필요 없으므로 종료)
            if arr[x][y] == 0:
                answer[0] += 1
            else: 
                answer[1] += 1
            
            return 
        
        zero_cnt = 0 # 0의 개수  
        one_cnt = 0 # 1의 개수 
        for i in range(x, x+l):
            for j in range(y, y+l):
                if arr[i][j] == 0:
                    zero_cnt += 1
                else: 
                    one_cnt += 1
        if zero_cnt == l*l:
            # 방문처리하기 
            check_visited(x, y, l)
            answer[0] += 1
            return 
        if one_cnt == l*l:
            check_visited(x, y, l)
            answer[1] += 1
            return 
        # 0, 1 섞여있는 경우 
        l = l//2
        compress(x, y, l)
        compress(x, y + l, l)
        compress(x + l, y, l)
        compress(x + l, y + l, l)
    
    compress(0, 0, n)
    return answer