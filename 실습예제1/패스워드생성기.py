# Password Generator Project
import random
# 영문 대소문자 , 숫자, 특수문자 리스트에 저장
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("파이썬 비밀번호 생성기!")
nb_letters = int(input("몇개의 영문자? "))
nb_symbols = int(input("몇개의 특수문자? "))
nb_numbers = int(input("몇개의 숫자? "))

# 패스워드를 저장할 리스트를 생성
password_list = []

# 영문자 개수만큼 반복문
for i in range(nb_letters):
    password_list.append(random.choice(letters))
    # 비밀번호 리스트에 문자열리스트에서 랜덤으로 하나 추가


# 아래에 특수문자와 숫자도 패스워드 리스트에 추가하는 코드 작성 👇
for s in range(nb_symbols):
    password_list.append(random.choice(symbols))


for n in range(nb_numbers):
    password_list.append(random.choice(numbers))
# 위에 특수문자와 숫자도 패스워드 리스트에 추가하는 코드 작성 👆

# print(password_list)
# 셔플하면 리스트의 순서를 랜덤으로 재설정
random.shuffle(password_list)
# print(password_list)

password = ""
for c in password_list:
    password += c

print(f"생성된 패스워드 : {password}")
