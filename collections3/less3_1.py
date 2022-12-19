# A Азбука ///////////

# vol_word = int(input())
#
# is_has = "YES"
#
# while vol_word > 0:
#     data = input()
#
#     vol_word -= 1
#     if is_has == "NO":
#         continue
#     if not data.startswith("а") and not data.startswith("б") and not data.startswith("в"):
#         is_has = "NO"
#
# print(is_has)


# B Кручу-верчу ////////

# strng = input()

# for i in input():
#     print(i)


# C Анонс новости ///////


# length_head = int(input())
#
# value_head = int(input())
#
# head = []
# char = "..."
#
# while value_head > 0:
#     head.append(input())
#     value_head -= 1
#
# for i in head:
#     if len(i) < length_head - len(char):
#         print(i)
#         continue
#     print(i[:22] + char)


# D Очистка данных /////////

# start_char = "##"
# end_char = "@@@"
# data = []
#
# while (string := input()) != "":
#     if string.endswith(end_char):
#         continue
#     elif string.startswith(start_char):
#         data.append(string[2:])
#     else:
#         data.append(string)
#
# for i in data:
#     print(i)


# E А роза упала на лапу Азоро 4.0

# string = input()
#
# print("YES") if string == string[::-1] else print("NO")


# G А и Б сидели на трубе

# num = sum([int(x) for x in input().split()])
#
# print(num)


# H Зайка 7

# volume = int(input())
#
# data = []
# search = "зайка"
#
# for i in range(volume):
#     string = input()
#     length = string.find(search)
#     data.append(length + 1) if length != -1 else data.append("Заек нет =(")
#
# for i in data:
#     print(i)


# I Без коментариев ///////

# char = "#"
# data = []
#
# while (string := input()) != "":
#     if string.startswith(char):
#         continue
#     if (index := string.find(char)) != -1:
#         data.append(string[:index])
#     else:
#         data.append(string)
#
# for i in data:
#     print(i)


# J  Частотный анализ на минималках ////////

# from collections import Counter
#
# stop = "финиш"
# new_data = []
#
# while (string := input().lower()) != stop:
#     new_data.extend(string.split())
#
# cnt = dict(Counter(''.join(new_data)).most_common(1))
#
# for key in cnt.keys():
#     print(key)


# K Найдется все
# import itertools
#
# vol_page = int(input())

# data = []
#
# for i in range(vol_page):
#     data.append(input())
#
# search = input()
#
# for i in data:
#     if i.lower().find(search) != -1:
#         # new_data = re.split(r'\W+', i.lower())
#         # print(new_data)
#         # if search in new_data:
#         print(i)


# L Меню питания
# import itertools
# from itertools import cycle
#
# porridge_list = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
#
# volum_day = int(input())
#
#
# for i, j in enumerate(cycle(porridge_list)):
#     print(j)
#     if i >= volum_day - 1:
#         break


# М Массовое возведение в степень

# Индийский способ возведения

# d = int(input())
# s = int(input())
# p = 1
# b = bin(s)[2:]
# for x in b:
#     p *=p
#     if x == '1':
#         p *= d
#
# print(p)

#


# num_volume = int(input())
#
# num_list = []
#
# for i in range(num_volume):
#     num_list.append(int(input()))
#
# num_pow = int(input())

a = int(input())
n = int(input())

res = 1

mult = a

while n != 0:
    if n % 2 == 1:
        res *= mult
    mult = mult * mult
    n = n / 2


print(res)
