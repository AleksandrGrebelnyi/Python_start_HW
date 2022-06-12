# Число-палиндром с обеих сторон (справа налево и слева направо) читается
# одинаково. Самое большое число-палиндром, полученное умножением двух
# двузначных чисел: 9009 = 91 × 99. Найдите самый большой палиндром, полученный
# умножением двух трехзначных чисел. Выведите значение этого палиндрома и то,
# произведением каких чисел он является.

def find_biggest_3digits_palindrom():
    maximum_palindrom = 0
    for i in range(900, 1000):
        for j in range(900, 1000):
            c = i * j
            s = str(c)
            s_revers = s[::-1]
            if s_revers == s and c > maximum_palindrom:
                maximum_palindrom = c
                i_res = i
                j_res = j
    return f"{i_res} * {j_res} = {maximum_palindrom} => It's the biggest palindrom of 3 digits number"


print(find_biggest_3digits_palindrom())





# n = 9009
# list_number = list(str(n))
# if list_number == list_number[::-1]:
#     print('Yeas')
# else:
#     print('No')
#
#
#



# n = 9009
# n_res = n
# c_n = ''
# while n != 0:
#     r = n % 10
#     c_n += str(r)
#     n //= 10
#
# c_n = int(c_n)
# if n_res == c_n:
#     print('Gooood')
# else:
#     print('Nooo')
