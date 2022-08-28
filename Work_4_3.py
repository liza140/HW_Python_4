# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 0.001 -> 3.142
# 0.00001 -> 3.14159

import math

N = float(input("Ввеолите точность числа Пи в виде десятичной дроби: "))

def find_exact(n):
    count = 0 
    while n < 1:
        n = n*10
        count +=1
    return count

col = find_exact(N)

print(round(math.pi, col))


