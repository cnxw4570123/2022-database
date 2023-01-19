# print(1+1)
# import random
# import math

# print(math.pow(8, 2))

# print(random.random())

students = ["egoing", "sori", "maru"]
grades = [2, 1, 4]
print(students[1])

str = ''
if str:
    print('문자열 있음')
else:
    print('아님')


class Stack:
    def __init__(self):
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()


stack = Stack()
print(len(stack))
stack.push(100)
print(len(stack))
print(bool(stack))

stack.pop()
print(len(stack))
print(bool(stack))
var = 'Hello' or []  # 참의 논리를 갖는 값을 가짐
print(var)  # Hello 출력


def sgn(x):
    return 1 if x > 0 else (0 if x == 0 else -1)  # 3항 연산자


print(sgn(2))
print(sgn(0))
print(sgn(-1))

for i in range(0, 12, 2):  # 2씩 변화하며 출력
    print(i)

arr = ['a', 'b', 'c', 'd']
for x in arr:
    print(x)

i = 0
while i < 10:
    print(i)
    i += 1


def function(*args):
    print(args)


function(1, 2, 3, 4)

l = [1, 2, 3]  # 리스트 -> 순서가 있고 가변
t = (1, 2, 3)  # 튜플 -> 순서가 있고 불변
list = [1, 'hello', 3, 3.15, True, [6, 7, 'str']]  # 자료형 여러 개 가능

# 슬라이싱 -> [start:stop:step]
print(list[:])  # 슬라이싱 -> 모든 요소 출력
print(list[2:])  # 2번 인덱스부터 끝까지 출력

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a + b)

a = ['a', 'b', 'c']
b = [1, 2, 3, 4]
print(a * 2)  # 리스트의 원소 복제
# 리스트에서 곱연산은 원소를 곱하는 것이 아닌 리스트 자체를 복사

# 튜플
print("튜플")
mytuple = (1, 2, 3)
mytuple = tuple([1, 2, 3])

print(mytuple)
# , 으로 생성
mytuple = 1, 2, 3

# 단일 요소로 튜플 생성 시에는 , 반드시 붙이기
mytuple = 1,
print(type(mytuple))

mytuple = 1
print(type(mytuple))

mytuple = (1)
print(type(mytuple))

mytuple = (1.2345,)
print(type(mytuple))

print(f'{mytuple[0]:.1f}') #f-string 문자열 표기법
# 표기시 :.nf로 자리수 지정 가능