# 1. Дано число. Проверить, является ли оно «счастливым билетом».
# Примечание: счастливым билетом называется число, в котором, при четном
# количестве цифр в числе, сумма цифр его левой половины равна сумме цифр
# его правой половины. Например, рассмотрим число 1322. Его левая половина
# равна 13, а правая 22, и оно является счастливым билетом (т. к. 1 + 3 = 2 + 2).
# 3 variants of solution

x = input('Ticket number is => ')
x = list(map(int, x))

mid = len(x) // 2
if len(x) % 2:
    res = sum(x[:mid]) == sum(x[mid + 1:])
    print(res)
else:
    res = sum(x[:mid]) == sum(x[mid:])
    print(res)


# n = int(input('Enter ticket number: '))
# s = list(map(int, str(n)))  # use function map() to change type of variables
# if sum(s[:2]) == sum(s[2:]):
#     print('Lucky')
# else:
#     print('Ordinary')
#
#
# number = int(input('Enter ticket number: '))
# list_str_num = list(str(number))  # made list with str elements from int
# sp = []
# for i in list_str_num:
#     sp.append(int(i))  # made int in list to sum integers in the list
# print(sp)  # check that list consist from int numbers
# if sum(sp[:2]) == sum(sp[2:]):
#     print('Lucky ticket')
# else:
#     print('Ordinary ticket')
#


n = int(input('Enter number =>'))
s = str(n)
sp = [int(n) for n in s]
if not sum(sp) % 2:
    print('Lucky')
else:
    print('Ordinary')








