
# 🚨 여기는 그대로 👇
heights = input("학생들의 키를 입력하세요\n").split()
# split() => 기본공백(스페이스)로 입력된 값을 리스트로 저장
for n in range(0, len(heights)):  # 키의 숫자만큼 반복
    heights[n] = int(heights[n])  # 문자열 리스트를 숫자 리스트로 교체
# print(heights)
# 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇

total_height = 0
for height in heights:
    total_height += height
print(f"전체 키의 합 = {total_height}")
print(f"학생의 숫자는 {len(heights)}")
print(f"평균 키의 값은 : {total_height/len(heights)}")
