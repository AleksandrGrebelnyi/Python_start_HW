# Напишите функцию, которая реализует линейный поиск элемента в списке целых
# чисел. Если такой элемент в списке есть, то верните его индекс, если нет, то
# верните число «-1»

def find_element(sp, aim):
    for i, item in enumerate(sp):
        if item == aim:
            return i
    return -1


sp = [939, 23, 88, 5, 37, 56]
aim = 5
print(find_element(sp, aim))


# def find_element(sp, aim):
#     # return [element for element in range(len(sp)) if sp[element] == aim] Но как вывести -1 если элемента нет?
#     for element in range(len(sp)):
#         if sp[element] == aim:
#             return element
#     return -1
#
#
# sp = [939, 23, 88, 5, 37, 56]
# aim = 5
# print(find_element(sp, aim))


