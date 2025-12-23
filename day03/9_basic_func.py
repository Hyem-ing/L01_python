# 함수 기초

print('== 함수 사용 전 ==')
number1 = 5
number2 = 10

# 둘중에 뭐가 더 큰지 비교 -> 큰 값을 출력
if number1 > number2:
    answer = number1
else:
    answer = number2
print(answer)


number3 = 7
number4 = 4

# 뭐가 큰지 비교
if number3 > number4:
    answer = number3
else:
    answer = number4
print(answer)

# 똑같은 코드 다시 작성해야만 한다..
# 불필요함 / 비효율

print('=== 함수 사용 후 ===')

# 함수 정의 (define)
# 함수라고 하는 블럭을 만듦
def get_bigger(num1, num2):
    if num1 > num2:
        answer = num1
    else:
        answer = num2
    return answer
# 박스만 만들었기 때문에 아무일도 일어나지 않습니다.

# 함수 호출 (call)
# 함수 불러와서 사용
print(get_bigger(number1, number2))
print(get_bigger(number3, number4))

# print(len(5)) # TypeError
# print(get_bigger('abc', 123)) # TypeError