# https://school.programmers.co.kr/learn/courses/30/lessons/70129

s = "101101"

# 2진수로 변환하는 함수 
def change_to_binary(n):
    result = []
    
    while True:
        result.append(str(n%2))
        n //= 2
        if n == 1:
            result.append("1")
            break 
    
    return "".join(result[::-1])

print(change_to_binary(6))

"""
def remove_zero(s):
    cnt = s.count("0") # 0 의 개수 
    new_s = s.replace("0","")
    return new_s, cnt # str, int 

def change_to_binary(n):
    result = []
    
    while True:
        
        result.append(str(n%2))
        n //= 2
        if n == 1:
            break 
    
    return "".join(result[::-1])

def solution(s):
    answer = []
    binary_cnt = 0 
    zero_cnt = 0
    
    while True:
        if s == "1":
            break
        s, z_cnt = remove_zero(s)
        zero_cnt += z_cnt 
        s = bin(len(s))[2:]
        binary_cnt += 1
    
    return [binary_cnt, zero_cnt]
"""