# 반복문
# while 반복문

# while 조건식:
    # 반복되는 코드

# while True:
#     print('영원히 반복......!')

# while문에서 중요한 지점! 조건을 변화시킬수 있는 무언가가 중요하다.

numbers = [1,2,3,4,5]
i = 0

while i < len(numbers):
    print(numbers[i])
    # 조건을 변화시킬 수 있는 식이 꼭 필요하다. (증감식)
    i += 1

print(i) # 5 < 4 의 결과, while문의 조건이 False


# 조건문과 함께 사용한 값 필터링
print('======')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i < len(numbers):
    if i % 2 == 1: # 홀수 인덱스 케이스만 출력
        print(numbers[i])
    i += 1 # 증감식의 위치가 조건과 무관히 실행되기 때문에 

print('======')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

# while i < len(numbers):
#     if i % 2 == 1: # 홀수 인덱스 케이스만 출력
#         print(numbers[i])
#         i += 1 # 문제 발생!!! 
# if 문을 만족한 경우에만 조건이 바뀌지 않도록 주의


names = ['alex','ken','jun','chelsea','heather']

# NameError: name 'idx' is not defined.
# 할당되지 않은 변수를 조건식에 사용하였기 때문에 에러 발생
# while idx < len(names):
#     print(f'안녕하세요! {names[idx]}님!')
#     idx += 1

idx = 0
while idx < len(names):
    print(f'안녕하세요! {names[idx]}님!')
    idx += 1