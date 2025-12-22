# 컨테이너 자료형
# 튜플 (tuple)
# <class 'tuple'>

# 1. 순서가 존재하는 자료형
# 2. 불변 자료형

# 튜플 생성 
# 소괄호 내부에 값을 입력 / 각 값은 , 를 통해 구분
# (값, 값, 값)

numbers = (10, 20, 30, 40, 50)
print(numbers)
print(type(numbers))

# 연산 가능 (+, *)
# 연산 후에는 새로운 튜플을 만들어 낸다.
numbers_1 = (1,2)
numbers_2 = (3,4)
numbers_3 = numbers_1 + numbers_2
print(numbers_3)
print(type(numbers_3))

print(id(numbers_1))
print(id(numbers_2))
print(id(numbers_3))

# 특징 1 : 순서가 있는 자료형
# 튜플[인덱스] 로 각 값에 접근
print(numbers)
print(numbers[1])
print(numbers[-1])

# 튜플[시작:끝:간격] 슬라이싱 가능
print(numbers[1:4:2])
print(numbers[::-1])

# 특징 2 : 불변 자료형 (immutable)
# 불가능하다. 변경이

# numbers[1] = -1
# TypeError: 'tuple' object does not support item assignment