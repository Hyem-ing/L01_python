# 문자열 메서드

# 문자열
    # 순서 : O
    # 변경 : X
    # 중복 : O

word = 'merry christmas!!!!!!!'
print(word)
print(len(word))

# 문자열 분할 : split
# 특정한 구분자를 기준으로 문자열을 나눠서, 리스트를 반환
word_list = word.split(' ') # 자기자신을 바꾸지 않고, 리스트 반환
print(word_list)

# 언제 사용?
# students = input('학생의 이름 명단을 입력해 주세요.')
# students_list = students.split(',')

# print(type(students_list))
# print(students_list)

# 문자열 합치기 : join()
# 특정 구분자로 이어 붙이기
string_list = ["merry", "christmas", 'happy','holiday','!!']
print(len(string_list))

string_join = " ".join(string_list) # 12 , 25 등의 숫자가 포함되면 연결지어주지 않음
print(string_join)
print(type(string_join))
