# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

from cgi import print_arguments
import math

N = int(input("Введите натуральное число: "))
half = round(N/2)+1

def fill_list (h):
    prime = []
    for i in range(2, h):
        prime.append(i)
    return prime

list_N = fill_list (half)
print("Исходный список: ", list_N)

def prime_list (list):
    new_list = []
    for i in range(0, len(list)):
        if list[i] != 0:
            new_list.append(list[i])
            p = list[i]
            for j in range(i+p, len(list), p):
                list[j] = 0
    return new_list

def prime_factors(new_list, n):
    fact = []
    for i in range(0, len(new_list)):
        while n % new_list[i] == 0:
            fact.append(new_list[i])
            n = n/new_list[i]
    if n == 1:
        print(f"Простые множители числа {N}: {fact}")
    else:
        print(f"число {N} невозможно разложить на простые множители")


prime_l = prime_list(list_N)
# print(list_N)
print("Список простых чисел: ", prime_l)

prime_factors(prime_l, N)





