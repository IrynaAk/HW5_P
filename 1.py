# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = int(input("Введите точность (!количество знаков после запятой от 1 до 10!): \n"))
d_num = 10 ** -d
# accuracy_num_digits = len(str(d))

# print(accuracy_num_digits)
# print(d_num)
pi_const = 3.1415926535897932

pi_accurate = 1

for i in range(1, 40):
    pi_calc = 2*(3**0.5)
    pi_accurate = pi_accurate + 1/((2 * i + 1) * (-3) ** i)
    pi_calc = pi_calc * pi_accurate
    if abs((pi_const / d_num) - (pi_calc / d_num)) <0.001:
        print(f'π = {math.floor(pi_calc*(10**d))/(10**d)}, number of iterations: {i}')
        break

