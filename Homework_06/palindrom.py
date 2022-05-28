# С клавиатуры вводится число. Проверить, является ли оно палиндромом.
# Примечание: палиндромом называется число, слово или текст, которые
# одинакового читаются слева направо и справа налево. Например, это числа
# 143341, 5555, 7117 и т. д.

number = int(input('Enter your number: '))
list_number = list(str(number))  # made type(list with elements str) from type (int)
if list_number == list_number[::-1]:  # compare in both directions
    print('Palindrome')
else:
    print('Ordinary')