# while 문 간단실습
# 1. 1~10 더한 값 55 출력하기
answer = 0
num = 1

while num <= 10: # 조건으로 활용
    # answer = answer + "1"
    # answer = answer + "2"
    # ...
    # answer = answer + "10" -> 조절하고자 하는 숫자
    answer += num
    num += 1      # 증감

print(answer)
print(num) # 11 <= 10 -> False로 반복 종료

# 2. while문과 조건문을 사용하여, 짝수인 경우만 더한 값을 출력하기
answer = 0
num = 1

while num <= 10: # 조건으로 활용
    # 짝수인 경우에만 더하기
    #   answer = answer + "2"
    # ...
    #   answer = answer + "10"
    if num % 2 == 0:
        answer += num
    num += 1      # 증감

print(answer)