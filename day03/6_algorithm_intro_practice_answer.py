# 떡잎마을 반장선거
# 후보가 없는 반장선거 
# 표가 발생하면, 자동 입후보 되는 구조

votes = ['짱구','짱구','수지','짱구','훈이','맹구','짱구',
        '수지','수지','수지','짱구','유리','철수']

# 누가 반장이 될까요?
result = {} # 빈 딕셔너리
# for vote in votes:
    # result[vote] += 1 # KeyError: '짱구'
    # result[vote] = result[vote] + 1 # 복합 연산

for vote in votes:
    if vote not in result: # 입후보 안된 경우에만, 입후보 하면서 1표 집계
        result[vote] = 1
    else:
        result[vote] += 1
print(result) # 집계 완료!

# 최다 득표 인원 찾기 (동점 없을 때)
max_counts = 0
max_name = ""

for k,v in result.items():
    if v > max_counts:
        max_counts = v
        max_name = k

print(f'반장은 {max_counts}표 득표한 {max_name}가 되었습니다.')