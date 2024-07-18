from itertools import combinations
def solution(friends, gifts):


    give_log = {f : {f:0 for f in friends} for f in friends} # {'muzi': {}, 'ryan': {}, 'frodo': {}, 'neo': {}}
    receive_log = {f : {f:0 for f in friends} for f in friends} 

    for gift in gifts: 
        gift = gift.split()
        giver, receiver = gift[0], gift[1]
        give_log[giver][receiver] += 1 # 준 기록 
        receive_log[receiver][giver] += 1 # 받은 기록 

    give_sum = {f : sum(give_log[f].values()) for f in friends}
    r_sum = {f : sum(receive_log[f].values()) for f in friends}
    receive_sum = {f: 0 for f in friends}

    for comb in combinations(friends, 2):
        print(comb)
        me, friend = comb 
   
        if give_log[me][friend] > receive_log[me][friend]:
            receive_sum[me] += 1
        elif give_log[me][friend] < receive_log[me][friend]:
            receive_sum[friend] += 1
        else:
            
            my_gift_score = sum(give_log[me].values()) - sum(receive_log[me].values())
            friend_gift_score = sum(give_log[friend].values()) - sum(receive_log[friend].values())
       
            if my_gift_score > friend_gift_score:
                receive_sum[me] += 1
            elif my_gift_score < friend_gift_score:
                receive_sum[friend] += 1
            else:
                continue 

    # 가장 많이 선물을 받은 개수 반환 
    return max(receive_sum.values())