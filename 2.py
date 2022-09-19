# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

a = int(input('please type a number: '))

def Factor(n):
    l = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            l.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        l.append(n)
    return l

print(Factor(a))



