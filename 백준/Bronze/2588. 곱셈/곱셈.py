a = int(input())
b = int(input())

num1 = a * (b % 10)
num2 = a * ((b % 100) // 10)
num3 = a * (b // 100)
num4 = a * b

print(num1, num2, num3, num4, sep="\n")