# Реализуйте функцию, параметрами которой являются - два числа и строка.
# Возвращает она конкатенацию строки с суммой чисел

def concatenate_str_with_numbers(n1, n2, str_1):
    if not isinstance(n1, int) or not isinstance(n2, int) or not isinstance(str_1, str):
        return None
    res = n1 + n2
    return str(res) + str_1


print(concatenate_str_with_numbers(5, 7, 'Hello'))