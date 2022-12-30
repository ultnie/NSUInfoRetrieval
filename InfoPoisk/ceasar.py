import os.path

def encrypt(text, lang, n):
    up = lang.upper()
    low = lang.lower()
    lgt = len(lang)
    result = ""
    for ch in text:
        if ch in up:
            result += up[(up.find(ch) + n) % lgt]
        elif ch in low:
            result += low[(low.find(ch) + n) % lgt]
        else:
            result += ch
    return result


eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

input_f_str, n_str, lang = input().split(sep=" ")
n = None
input_f = None
result = None

if os.path.exists(os.path.dirname(input_f_str)):
    input_f = open(input_f_str, "r", encoding="utf-8")
else:
    print("Неправильный путь к файлу")
    exit(1)

if n_str.isdigit():
    n = int(n_str)
else:
    print("Второй аргумент не является числом")
    exit(1)

if lang == "eng":
    result = encrypt(input_f.read(), eng, n)
elif lang == "rus":
    result = encrypt(input_f.read(), rus, n)
else:
    print("Доступные языки указываются как eng или rus")
    exit(1)

input_f.close()
output_f = open(input_f_str+" encrypted.txt", "w", encoding="utf-8")
output_f.write(result)
output_f.close()