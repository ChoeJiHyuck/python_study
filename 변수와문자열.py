# 여러개의 변수를 동시에 초기화
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# 예제 2
x = 10
print(x)

# 예제 3
x, y, z = 1, 2, 3
print(x, y, z)  # 출력시 변수 여러개 가능

# 예제 4
x, y, z = 1, 2.0, '냐'
print(type(x), type(y), type(z))

# 예제 5
a = input("a: ")
b = input("b: ")
a, b = b, a
print("a : " + a)
print("b : " + b)
