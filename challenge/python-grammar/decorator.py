import time 

"""
함수 또는 클래스에 기능을 추가하는 방법 중 하나로, 
기존 코드를 수정하지 않고도 동작을 확장할 수 있게 해줍니다
"""

### 1. function 확장 

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time}")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("slow function ran")

slow_function()

### 2. class 확장
def class_decorator(cls):
    class WrappedClass:
        def __init__(self, *args, **kwargs) -> None:
            self.wrapped = cls(*args, **kwargs)
        
        def __getattribute__(self, name: str):
            return getattr()
    return WrappedClass


            