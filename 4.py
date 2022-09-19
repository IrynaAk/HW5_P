# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = random.randint(0, 100)

k = int(input("Введите натуральную степень k: "))
list_koef = []

for i in range(k):
    if (k - i) > 1:
        degr = str(k - i)
        add = '*x^'
    else:
        degr = ''
        add = '*x'
    list_koef.append(str(random.randint(0, 100)) + add + degr)      # change to random

final_str = ''

for i in range(len(list_koef)):
    final_str = final_str + list_koef[i] + ' + '

last_element = str(random.randint(0, 100))
final_str = final_str + last_element + " = 0"

with open('Task4.txt', 'w') as data:
    data.write(final_str) 





