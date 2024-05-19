# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate(arr):
    m = len(arr)
    result = [[0] * m for _ in range(m)] # 회전 결과 담기 
    
    for i in range(m):
        for j in range(m):
            result[j][m - i -1] = arr[i][j]
    
    return result 

def check(n, arr):
    for i in range(n, n*2):
        for j in range(n, n*2):
            if arr[i][j] != 1:
                return False 
    return True 

def solution(key, lock):
    n, m = len(lock), len(key)
    extended_lock = [[0] * (n * 3) for _ in range(n*3)] # 3 배로 확장시키기 
    
    for i in range(n):
        for j in range(n):
            extended_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4): #4 가지 방향으로 회전하기 
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                
                for kx in range(m):
                    for ky in range(m):
                        extended_lock[x+kx][y+ky] += key[kx][ky]
                
                # check 
                if check(n, extended_lock): # true 
                    return True 
                
                for kx in range(m):
                    for ky in range(m):
                        extended_lock[x+kx][y+ky] -= key[kx][ky]
    
    return False 