# 메서드 (method)
# 특정 자료형에 딸려 있는 함수

# 리스트
    # 순서 : O
    # 변경 : O
    # 중복 : O

numbers = [10,20,30,40,50]
print(id(numbers))

# 추가 : append 메서드
# 가장 마지막 위치에 새로운 원소 (딱 하나만) 추가
numbers.append(60) # 반환값이 없다.
print(numbers)
print(id(numbers)) # numbers 자체를 변경 -> 주소값 변화 없음

# 질문
# numbers.append([70,80,90])
# print(numbers) # [10, 20, 30, 40, 50, 60, [70, 80, 90]] -> 통으로 들어감
# print(numbers[-1])

# 여러 값을 추가하여 사용하고 싶다면? 다른 메서드

# 여러 값 추가 : extend()
numbers.extend([70,80,90])
# numbers.extend(70,80,90) 
# TypeError: list.extend() takes exactly one argument (3 given)
print(numbers)

# 삽입 : insert()
# 특정 위치에 특정 값을 추가
numbers.insert(3,10000)
print(numbers)

# 삭제 : pop 메서드
# 위치를 기준으로 리스트 내 요소 삭제 / 삭제된 요소를 반환
deleted_value = numbers.pop(1)
print(deleted_value)
print(numbers)

# 삭제 : remove 메서드
# 값을 기준으로 삭제
numbers.remove(10000)
print(numbers)

# 값 세기 : count 메서드
# 중복이 가능하기 때문에 
numbers.extend([10,10,20,40])
print(numbers)
cnt = numbers.count(10) # 리스트 자체를 바꾸지 않습니다.
print(cnt)

# 정렬 : sort() 메서드
# sorted 내장함수와의 차이점
# 내장함수 sorted() : 전달받은 컨테이너를 정렬하여, "새로운 리스트"를 반환
# 메서드 sort() : 기존의 리스트 자체를 변경 -> 정렬한다.
numbers.sort(key=lambda x:-x)
print(numbers)

numbers.sort(key=lambda x:(x%3,-x)) # 두가지 기준으로 정렬
print(numbers)