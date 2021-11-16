# 숫자 맞추기 게임
import random
import art  # 로고가 들어있는 모듈

print(art.logo)  # 로고 출력
print("당신의 이름은 ?")
name = input()

print(f"안녕하세요 {name}님 1에서 20까지 숫자중 하나를 생각합니다.")
secretNumber = random.randint(1, 20)  # 랜덤으로 숫자 하나 생성

for count in range(1, 7):  # 6번의 맞출기회
    guess = int(input("맞춰보세요 \n"))
    # 괄호(  ) 안에 알맞는 내용을 작성하여 완성하세요 👇
    if (secretNumber > guess):
        print('그 숫자보다 큰수')
    elif (secretNumber < guess):
        print('그 숫자보다 작은수')
    else:
        break  # 반복문으 빠져나옴


if guess == secretNumber:
    print(f'잘 맞췄어요 {name}님 {count} 번만에 맞췄어요 !')
else:
    print(f'틀렸네요. 정답은 {secretNumber} 입니다.')
