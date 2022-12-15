# # N Простая задача ///////////
#
# num = int(input())
#
# lst = [2]
#
# for i in range(3, num + 1, 2):
#     if (i > 10) and (i % 10 == 5):
#         continue
#     for j in lst:
#         if j*j-1 > i:
#             lst.append(i)
#             break
#         if i % j == 0:
#             break
#     else:
#         lst.append(i)
# print(lst)
#
# Flag == False
#
# while num > 2:
#     if num == 2:
#         Flag = True
#         break
#     d = 3
#     for i in range(d, num+1, 2):
#         if i > 10 and i % 10 == 0:
#             break
#         for j
#
#         if i * i > num:
#             Flag = True
#             break

# O Зайка - 4 //////////

# num_landscape = int(input())
#
# search = "зайка"
#
# count = 0
#
# while num_landscape > 0:
#     num_landscape -= 1
#     string = input().split(" ")
#     if search in string:
#         count += 1
# print(count)


# P Полиндром

# num = input()
#
# index = len(num)
# start = 0
# end = 0
# if index % 2 == 0:
#     i = index / 2
#     start = num[:i]
#     end = num[:i:-1]
#
# print(start)
# print(end)