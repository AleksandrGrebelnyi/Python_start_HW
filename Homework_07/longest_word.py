# Вводится строка из слов, разделенных пробелами. Найти самое длинное
# слово и вывести его на экран. Added displayed list of lengths and number the longest word

t = input('Enter text with spaces: ').split()
print(f'Longest word is => {max(t, key=len)}')


# t = input('Enter text with spaces: ').split()
# res = list(map(lambda x: len(x), t))
# print(f'Longest word is => {max(t, key=len)}\nAmount of numbers => {res}\nLongest word => {max(res)}')



