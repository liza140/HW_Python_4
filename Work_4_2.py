# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

from logging import debug

def read_file():
    ice_p = None
    ice_n = None
    with open('icecream.txt', "r", encoding='utf-8') as file:
        ice_p = file.readlines(1)
        ice_n = file.readlines(2)
    return ice_p, ice_n

ice_pos, ice_neg = read_file()
ice_pos = ice_pos[0].split(', ')
last = ice_pos[3].split('\n')
ice_neg = ice_neg[0].split(', ')

def del_n(list, el):
    list.pop(3)
    list.append(el[0])
    return list

ice_pos = del_n(ice_pos, last)
ice_pos = set(ice_pos)
ice_neg = set(ice_neg)

print("Закончилось: ", ice_pos.difference(ice_neg))

