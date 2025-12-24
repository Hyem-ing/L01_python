# 반환값과 매개변수 유무

# 반환값 X, 매개변수 O
# 선언할 때는 실행 X
def hello(name):
    print('함수 안에서 출력') # 2-1
    print(f'안녕하세요! {name}님') # 2-2

print('함수 밖에서 출력') # 1
print(
        hello('jun') # 2
        
        ) # 3 -> hello 함수가 반환하는 것이 없기 때문에 None 출력

# 매개변수와 반환값은 함수를 구성할때 필수 요소는 아니다.
# 즉, 없어도 함수를 정의할 수 있다.
# 원하는 설계에 따라 선택하여 사용하면 된다.

# [간단 실습] 별 찍기
print('===== 별 찍기 =====')
# 자연수 N을 입력받아, N줄까지 별을 출력하는 함수를 만드시오.
# 첫 번째 줄은 별이 1개이며, N번째 줄은 N개의 별이 찍혀야 합니다.

# ex) 만약 N이 3 이라면?
# *
# **
# ***

N = int(input('정수를 입력해 주세요 : '))

# 함수 정의 (define)
# 매개 변수 O, 반환값 X
def print_stars(n):
    for i in range(1,n + 1): # 반복하여, 한줄씩 찍기
        print('*' * i) # 별 n개를 출력하기 위해 문자열 "*" 곱하기 연산 
        # i = 1 / "*" * 1 => "*" 
        # i = 2 / "*" * 2 => "**"
        # i = 3 / "*" * 3 => "***"

print_stars(N)

# 잘못된 케이스 1 : 입력 받아야 되는데, 입력 받지 못함
# TypeError: print_stars() missing 1 required positional argument: 'n'
# print_stars()

# 잘못된 케이스 2 : 반환받는 것이 없는데, 값을 달라고 함
# print(print_stars(N))
# 파이썬에서 자체적으로 없다 -> None