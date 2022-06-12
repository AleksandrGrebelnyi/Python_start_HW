# Существуют такие последовательности чисел:
# 0,2,4,6,8,10,12 след 14 (+2)
# 1,4,7,10,13 след 16 (+3)
# 1,2,4,8,16,32 след 64 (*2)
# 1,3,9,27  след 81 (*3)
# 1,4,9,16,25 след 36 (3 + 2 + 2....)
# 1,8,27,64,125 кубическая последовательность 216
# Реализуйте программу, которая выведет следующий член этой последовательности
# (либо подобной им) на экран. Последовательность пользователь вводит с
# клавиатуры в виде строки. Например, пользователь вводит строку 0,5,10,15,20,25 и
# ответом программы должно быть число 30.

def next_number_of_sequence(s):
    n = list(map(int, s.split(',')))
    last_number = n[-1:]
    penultimate = n[len(n)-2:-1]
    pre_penultimate = n[len(n)-3:-1]
    if last_number[0] - penultimate[0] == 2:
        return 2 + last_number[0]
    elif last_number[0] - penultimate[0] == 3:
        return 3 + last_number[0]
    elif last_number[0] / penultimate[0] == 2:
        return 2 * last_number[0]
    elif last_number[0] / penultimate[0] == 3:
        return 3 * last_number[0]
    elif (last_number[0] - penultimate[0]) - (penultimate[0] - pre_penultimate[0]) == 2:
        return (last_number[0] - penultimate[0]) + 2 + last_number[0]
    else:
        return round((last_number[0] ** (1/3) + 1)) ** 3


s = '1,2,4,8,16,32'
print(next_number_of_sequence(s))


