
# global - 함수 밖에서 선언된 전역 변수를 가리키기

# my_var = 100

# def print_var():
#     global my_var # global 키워드를 사용하면 test() 함수 밖에서 선언된 전역 변수를 가리키게 된다. 
#     print(my_var)

# print_var()
# print(my_var)

'''
100
100
'''

# nonlocal - 동일한 이름의 새로운 변수가 생성되는 것을 방지, 중첩 함수 내서 비지역 변수 대상으로 사용함 
def print_num():
    num = 0 
    
    def change_num():
        nonlocal num # 함수 밖에서 선언된 변수를 참조하여 값을 변경함. 
        num = 100 
        print(num) # 100 
    change_num()
    print(num) # 100 
print_num()
    
    

