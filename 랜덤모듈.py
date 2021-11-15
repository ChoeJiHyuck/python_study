# 랜덤 모듈 불러오기
import random
import myModule as my

x = random.randint(0, 1)  # 0,1의 랜덤 숫자 생성
# 동전을 던졌을때 랜덤으로 앞 뒷면이 나오도록 코드 작성
if x == 1:
    print("앞면")
else:
    print("뒷면")

# 내가 만든 마이모듈의 변수 pi를 불러옴
print(my.pi)
