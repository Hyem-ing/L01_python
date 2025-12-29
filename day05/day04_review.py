# 복습
# 다양한 자료를 이용하여, 정보를 구조화하는 방식이 알고리즘에서 중요하다.

# 복습 실습
# users -> dict
# users['total_user'] -> int
# users['information'] -> list
    # list의 값 -> dict
users = {
        'total_user': 3,
        'information': [
            {'name': 'alex', 'age':3, 'license':True},
            {'name': 'june', 'age':7, 'license':False},
            {'name': 'peter', 'age':4, 'license':False}
        ]
        }

# 구조 확인
print(type(users))
print(users.keys()) # 키-값의 한쌍 구조로 만들어진, 순서가 없는 컨테이너 자료형

print(users['total_user']) # int
print(users['information']) # list -> 순서가 존재하는 컨테이너 자료형

# 사람들의 정보만 뽑아보기
infos = users['information'] # 리스트만 뽑아서 할당
print(infos[0]) # 순서가 존재하기 때문에 숫자(위치)로 값 접근

# Q1. 라이센스가 있는 인원들의 숫자 구하기
# => 라이센스 == True 인 사람의 수 (세기)
cnt = 0 # 초기값

print('= Q1 =')
# for info in users['information']: # 동일
for info in infos:
    # print(type(info))
    if info['license'] == True:
        cnt += 1

print(f'라이센스가 있는 인원 : {cnt} 명') # f-string

# Q2. 모든 사람의 나이 평균 구하기
print('= Q2 =')

# 방법 1 : 숫자형 변수와 복합 연산 활용
age_sum = 0

for info in infos:
    age_sum += info['age'] # 복합연산

ave_age = age_sum / users['total_user']
print(f'나이의 평균은 {ave_age} 살입니다.')

# 내장함수로 반올림 가능
print(f'나이의 평균은 {round(ave_age, 2)} 살입니다.')

# 방법 2 : 리스트와 내장함수 사용
# 평균 = 합산 / 갯수 -> ave = sum() / len()
age_lst = [] # 빈 "리스트" 생성 -> 순서 O, 변경 O, 중복 O

for info in infos:
    age_lst.append(info['age'])

print(age_lst)
print(sum(age_lst)/len(age_lst))

# 방법 3 : 리스트 컴프리헨션 (심화)
age_lst_comp = [info['age'] for info in infos]
print(sum(age_lst_comp)/len(age_lst_comp))

# Q3. 라이센스가 없는 "사람들의 이름 모으기"
# 리스트 -> 컨테이너 자료형 선택
name_lst = [] # 빈 리스트 생성

for info in infos:
    if info['license'] == False:
        name_lst.append(info['name'])
        
print(name_lst)

# 왜 이렇게까지 복잡하게 "구조화"해야 하는가?
# 구조화 된 형태의 장점

print(users)

# 추가 유저가 생길 때, 관리가 용이
# 전체 수 업데이트
print(users['total_user'])
users['total_user'] += 1
print(users['total_user'])

# 유저 정보 업데이트
users['information'].append({'name':'ken','age':10,'license':True}) # 추가
print(users)