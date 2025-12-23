# 실습
print('== 점수 관리 ==')
# 딕셔너리 (dict)
# {key:value}

# (1) 딕셔너리 생성
score = {"국어":85,
        "영어":90,
        "수학":78}
print(score)
print(type(score))

# (2) 파이썬 점수 추가
score['파이썬'] = 100
print(score)

# (3) 출력 반복
# for 변수 in 컨테이너:
    # 반복코드
for k,v in score.items():
    print(f'{k} 점수는 {v}점입니다')

print('== 수강생 명단 ==')
# 집합 (set)
python_class = {"철수","영희","민수"}
data_class = {"영희","지현","민수"}

print(type(python_class))
print(type(data_class))

# (1) 두 강좌를 모두 수강하는 학생
# 교집합 확인
print(python_class & data_class)
print(python_class.intersection(data_class))

# (2) 파이썬 강좌만 수강하는 학생
# 차집합 확인
print(python_class - data_class)
print(python_class.difference(data_class))

# (3) 두 강좌 중 하나라도 수강한 학생
# 합집합 확인
print(python_class | data_class)
print(python_class.union(data_class))

# 집합은 수학의 집합을 기반으로 만들어 졌기 때문
