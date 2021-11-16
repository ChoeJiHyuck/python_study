# try / except

def div10(n):  # 10에 입력값을 나눈다
    try:
        return 10/n
    except:
        print('에러: 0으로 나눌수 없음')


print(div10(2))
print(div10(0))  # 0으로 나눌수 없다.
print(div10(5))
