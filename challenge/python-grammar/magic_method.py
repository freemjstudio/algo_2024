class MyClass: 
    def __init__(self, name) -> None:
        self.name = name 

    # print 함수에서 사용되는 객체의 출력 형식 정의함. 
    def __str__(self) -> str:
        return f"MyClass instance with name: {self.name}"

    def __del__(self):
        print("Object is being deleted!")

obj = MyClass("minji")
print(obj)

class MyNumber:
    def __init__(self, value) -> None:
        self.value = value 
    
    def __add__(self, other):
        return MyNumber(self.value + other.value)
    
    def __eq__(self, other):
        return self.value == other.value 

a = MyNumber(10)
b = MyNumber(20)
c = MyNumber(10)

result = a + b
print(result.value)

print(a==c)
print(result==c)