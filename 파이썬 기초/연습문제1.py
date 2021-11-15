# in 비교 연산자
# in : 리스트나 문자열 안에 있으면 참 없으면 거짓

list1 = [1, 2, 3, 4, 5]
string1 = "My name is AskPython"

print(5 in list1)
print("is" in string1)

# 1
a = "life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# 2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

i = 1
result = 0
while i <= 1000:
    if(i % 3 == 0):
        result += i
    i += 1
print(result)

# 3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성
# *
# **
# ***
# ****
# *****

n = 5
i = 1
while i <= n:
    print('*'*i)
    i += i
