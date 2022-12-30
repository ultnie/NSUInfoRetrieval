input_str = input("Введите целое число: ")
n = int(input_str)
for i in range(n):
    num = 1
    for j in range(n-i+1):
        print(" ", end="")
    for j in range(1, i+1):
        print(num, end=" ")
        num = num * (i - j) // j
    print()