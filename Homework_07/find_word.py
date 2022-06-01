# Вовочка сидя на уроке писал подряд одинаковые слова (слово может
# состоять из одной буквы). Когда Марья Ивановна забрала у него тетрадь,
# там была одна строка текста. Напишите программу, которая определит
# самое короткое слово из написанных Вовочкой. Например:
# aaaaaaa — Вовочка писал слово - «a»
# ititititit — Вовочка писал слово - «it»
# catcatcatcat — Вовочка писал слово - «cat»

t = 'catcatcatcatcat'
res = list(map(lambda x: ord(x), t))
sp = []
for item in res:
    if item in sp:
        break
    else:
        sp.append(item)
print(res)
k = ''.join(list(map(lambda x: chr(x), sp)))
print(k)
