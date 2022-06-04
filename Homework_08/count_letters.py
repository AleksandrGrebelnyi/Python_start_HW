# Напишите программу которая считает строку текста с клавиатуры и выведет на
# экран статистику, сколько раз какая буква встречается в этой строке. Например,
# для строки «Hello world» эта статистика выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т. д

s = input('Enter your text: ').replace(' ', '')
res = {}
for letter in s:
    if not res.get(letter):
        res[letter] = s.count(letter)
print(res)


s = 'Hello world'.replace(' ', '')
res = {}
for letter in s:
    if res.get(letter) is None:
        res[letter] = 1
    else:
        res[letter] = res[letter] + 1
print(res)

