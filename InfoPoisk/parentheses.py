import os.path


def check_only_par(str):
    check = "()"
    return all(ch in check for ch in str)


def check_par(str):
    num = 0
    for ch in str:
        if ch == "(":
            num += 1
        elif ch == ")":
            if num == 0:
                print(f"\"{str}\" - Неправильная последовательность")
                exit()
            else:
                num -= 1
    if num != 0:
        print(f"\"{str}\" - Неправильная последовательность")
    else:
        print(f"\"{str}\" - Правильная последовательность")


input_str = input("Введите путь к файлу или скобочную последовательность: ")

if not os.path.exists(os.path.dirname(input_str)):
    if not (check_only_par(input_str)):
        print("Строка не является путём к файлу или скобочной последовательностью")
        exit(1)
    else:
        check_par(input_str)
else:
    f_in = open(input_str, "r", encoding="utf-8")
    str_f = f_in.readline()
    if not (check_only_par(str_f)):
        print("Первая строка в файле не является скобочной последовательностью")
        exit(1)
    else:
        check_par(str_f)