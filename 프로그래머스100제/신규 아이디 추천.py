# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # step 1
    new_id = new_id.lower()
    # step 2 - 소문자, 숫자, -, _, . 만 허용하기 아니면 제거 
    step2 = ""
    for s in new_id:
        if s.isalnum() or s in ['-', '_', '.']:
            step2 += s
    # step 3 - . 가 2번이상 연속되면 .개로 치환하기
    step3 = ""
    count = 0 
    for s in step2: 
        if s != '.':
            if count == 0:
                step3 += s
            else:
                step3 += "."
                step3 += s
                count = 0 # 다시 0 으로 리셋하기 
        else:
            count += 1
    # step 4
    while True:
        if step3[0] == '.':
            step3.pop(0)
        elif step3[-1] == '.':
            step3.pop(-1)
        else: 
            break
    # step 5
    step4 = step3
    if len(step4) == 0:
        step4 = "a"
    step5 = step4 
    # step 6
    if len(step5) >= 16:
        step6 = 
    else: 
        step6 = step5
    
    # step 7 
    if len(step6) <= 2:
        
        return step6
    else: 
        return step6
