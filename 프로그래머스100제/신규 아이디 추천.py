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
    # step 4 : 마침표(.)가 처음이나 끝에 위치한다면 제거
    step4 = list(step3)
 
    while step4:
        if step4[0] == '.':
            step4.pop(0)
        if step4[-1] == '.':
            step4.pop()
        if step4[0] != '.' and step4[-1] != '.': 
            break
    # step 5 : 빈 문자열이라면, new_id에 "a"를 대입
    if len(step4) == 0:
        step4 = "a"
    step5 = "".join(step4)
    # step 6 : new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(step5) >= 16:
        step6 = list(step5[:15])
        while step6[-1] == ".":
            step6.pop()
        step6 = "".join(step6)
    else: 
        step6 = step5
       
    # step 7 
    if len(step6) <= 2:
        while len(step6) < 3:
            step6 += step6[-1]
        return step6
    else: 
        return step6
 