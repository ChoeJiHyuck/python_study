# 튜플(tuple은 순서가 있고 수정불가인 자료구조입니다. 중복가능
# 리스트와 틀린것이 수정불가 , 표신는 () 괄호

# 튜플을 리터럴로 만들기
fruit_tuple = ('사과', '오렌지', '망고')

# 값을 가져오기
print(fruit_tuple[1])

# 값은 수정불가
#fruit_tuple[1] = '포도'

# 길이(아이템 갯수)
print(len(fruit_tuple))

# 튜플의 삭제
del fruit_tuple  # 전체 삭제

# print(fruit_tuple) # 없으므로 에러발생

# SET 자료형
# set은 순서(인덱스)가 없고 중복이 되지 않는 자료구조
# 표시는 {}
fruit_set = {'사과', '오렌지', '망고'}

# set에 있는지 없는지 검사
print('사과' in fruit_set)

# set에 추가 add
fruit_set.add('포도')
fruit_set.add('포도')
fruit_set.add('포도')
fruit_set.add('사과')
print(fruit_set)

# set에서 제거
fruit_set.remove('포도')

# 클리어 set
fruit_set.clear()  # 모든 아이템 삭제
print(fruit_set)
