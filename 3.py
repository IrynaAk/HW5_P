# 3 Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


numbers = [1, 1, 2, 2, 3, 4, 5, 5, 5, 6]

def get_unique_numbers(numbers):
    num_res = []
    for item in numbers:
        if item not in num_res:
           num_res.append(item)
    return num_res

print(get_unique_numbers(numbers))

