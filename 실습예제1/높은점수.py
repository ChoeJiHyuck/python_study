
# 🚨 여기는 그대로 👇
scores = input("학생들의 성적을 입력 :\n").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
    # 성적 입력을 문자열로 받기 때문에 다시 정수로 변환해서 리스트에 입력
print(scores)
# 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇
highest_score = 0
lowst_score = 99999
# for n in scores:
#     if(n > highest_score):
#         highest_score = n
#     if(n < lowst_score):
#         lowst_score = n

# print(f"가장 높은 점수는 : {highest_score}")
# print(f"가장 낮은 점수는 : {lowst_score}")

print(f"가장 높은 점수는 : {max(scores)}")
print(f"가장 낮은 점수는 : {min(scores)}")
