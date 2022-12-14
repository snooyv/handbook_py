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


# lenght_head = int(input())
#
# value_head = int(input())
#
# head = []
#
# while value_head > 0:
#     head.append(input())
#     value_head -= 1
# new_str = head[0].ljust(lenght_head)
# print(new_str)
# for i in head:
#     print(i.ljust(lenght_head))

str = "Начался саммит по мировому климату"

result = str[:23] + "..."
print(result)