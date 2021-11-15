import random

바위 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

보 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

가위 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [가위, 바위, 보]

user_choice = int(input("가위는 0 바위는 1 보는 2 를 적어 주세요.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("컴퓨터 선택:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("잘못된 번호를 선택했어요 0 , 1, 2 중 선택하세요")
elif user_choice == 0 and computer_choice == 2:
    print("이겼습니다!")
elif computer_choice == 0 and user_choice == 2:
    print("졌습니다.")
elif computer_choice > user_choice:
    print("졌습니다.")
elif user_choice > computer_choice:
    print("이겼습니다!")
elif computer_choice == user_choice:
    print("비겼습니다.")
