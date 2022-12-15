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

num = sum([int(x) for x in input().split()])

print(num)