# 001 함수 만들기
import datetime
from datetime import datetime
import random


def add(a, b):
    print(f"{a} + {b} = {a+b}")


add(10, 5)

# 002 함수의 리턴


def add(a, b):
    return a+b


print(add(10, 5))

# 003 List 리스트
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']

first_color = rainbow[0]
print(f'무지개의 첫번째 색은 {first_color}이다.')

# 004 리스트 사용하기
first_color = rainbow[-1]
print(f'무지개의 마지막 색은 {first_color}이다.')

# 005 리스트 추가하기
list1 = [1, 2, 3]
list1.append(4)
print(list1)

list = [1, 2, 3]
list += [4]
print(list)

# 006 리스트 수정
number = [1, 2, 3, 4, 5]
n = 5
if n in number:
    print(f'{n}(이)가 리스트에 있다.')

# 007 리스트 지우기
list1 = [1, 2, 3]
del list1[1]
print(list1)

# 008 딕셔너리 만들기
days_in_month = {
    '1월': 31,
    '2월': 28,
    '3월': 31
}

print(days_in_month)

# 009 딕셔너리 입력 자료형
dict1 = {
    '이름': '홍길동',
    '번호': 1010,
    '취미': ["낮잠", "숨쉬기", "커피"]
}

print(dict1)

# 010 딕셔너리 수정하기
days_in_month['2월'] = 29
print(days_in_month)

# 011 딕셔너리 삭제하기
days_in_month['-1월'] = 97889789
print(days_in_month)
days_in_month.pop('-1월')
print(days_in_month)

# 012 딕셔너리와 반복문
days_in_month['4월'] = 30
days_in_month['5월'] = 31
print(days_in_month)

for key in days_in_month:
    print(key)

# 013 문자열 출력
for key, value in days_in_month.items():
    print(f'{key}은 {value}일이 있습니다.')

# 014 random 실습(choice)
list = ['빨', '주', '노', '초', '파', '남', '보']
random_element = random.choice(list)

print(random_element)

# 015 random 실습(randint)
random_number = random.randint(2, 6)

print(random_number)

# 016 문자열 출력하기(shuffle)
random.shuffle(list)

print(list)

# 017 datetime 실습
now = datetime.now()
date = now.strftime("%Y-%m-%d")
print(date)

# 018 문자열 실습
string1 = """다스베이더가 말했다.
    "내가 니 애비다!"
    그 말을 들은 루크는 '깜짝' 놀랐다."""
list1 = string1.split()
print(list1[4])

# 019 반복문 사용하기
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, day in enumerate(days):
    print(f'{i}월의 날짜수는 {days[i]}일 입니다.')

# 020 정수와 실수
a = 23
b = 5

div = a // b

print(f"a를 b로 나눈 몫은 {div}입니다.")

# 021 while 문 실습
numbers = [1, 2, 3]
length = len(numbers)
i = 0
while i < length:
    print(numbers[i])
    i = i + 1

# 022 enumerate
sizes = [33, 35, 34, 37, 32, 35, 39, 32, 35, 29]
for i, size in enumerate(sizes):
    if size == 32:
        print(f"사이즈 32인 바지는 {i+1}번째에 있다.")
        break

# 023 예외 try except
try:
    a = 3/0
except:
    print("0으로 나눌 수 없습니다.")

# 024 예외의 이름을 알고싶을때
try:
    a = 5
    b = 0
    c = a/b
except Exception as ex:
    print(f'다음과 같은 에러가 발생했습니다: {ex}')

# 025 bool 논리연산
if []:
    print("[]은 True입니다.")

if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")

if {}:
    print("{}은 True입니다.")

if {'abc': 1}:
    print("{'abc':1}은 True입니다.")

if 0:
    print("0은/는 True입니다.")

if 1:
    print("1은 True입니다.")

# 026 논리연산자 or
a = 1 or 10
b = 0 or 10

print(f"a:{a}, b:{b}")

# 027 리스트 실습 inselt, sort, reverse
list1 = [1, 2, 3, 4]

list1.insert(0, 8)
print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))
list1.sort()
print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))
list1.reverse()
print("list1을 거꾸로 정렬한 결과 : {}".format(list1))

# 028 문자열과 리스트
str = "오늘은 날씨가 흐림"

# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split(" ")

# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고,
# position에 저장하세요.
position = words.index("흐림")
words[position] = "맑음"  # 흐림을 맑음으로 수정

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요.
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = " ".join(words)

print(new_str)

# 039 리스트 slice
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

red_colors = rainbow[:3]

blue_colors = rainbow[4:]

print("red_colors의 값 : {}".format(red_colors))
print("blue_colors 값 : {}".format(blue_colors))
