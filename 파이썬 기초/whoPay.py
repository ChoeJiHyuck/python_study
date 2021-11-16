import random

names_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적습니다.\n")
names = names_string.split(",")


# print(names)
# print(len(names))

n = random.randint(0, len(names)-1)  # 랜덤 인덱스 숫자(사람수 만큼)

print(f"오늘 커피는 {names[n]}(이)가 쏩니다!")
