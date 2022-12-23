# D Кашееды /////////

# semol_porrg_vol = int(input())
# oatml_porrg_vol = int(input())
#
# sem_porr_licke_name = [input() for i in range(semol_porrg_vol)]
#
# oat_porr_licke_name = [input() for j in range(oatml_porrg_vol)]
#
# result = set(sem_porr_licke_name) & set(oat_porr_licke_name)
#
# print(len(result)) if len(result) else print("Таких нет")


# K Однофамильцы ////////

# vol_family = int(input())
#
#
# data = [input() for _ in range(vol_family)]
# result = 0
#
# for i in set(data):
#     count = 0
#     for name in data:
#         if i == name:
#             count += 1
#     if count > 1:
#         result += count
#
# print(result)


# L Однофамильцы 2 |||||||||||

vol_family = int(input())

data = {}
is_print = False

while vol_family:
    string = input()
    vol_family -= 1
    if string not in data:
        data[string] = 1
    else:
        data[string] += 1
        is_print = True

if not is_print:
    print("Однофамильцев нет")
else:
    for key, val in data.items():
        if val > 1:
            print(f'{key} - {val}')

# dict_data = {}
# for i in data:
#     if i not in dict_data:
#         dict_data[i] = 1
#     else:
#         dict_data[i] += 1
#
# flag = False
# for key, val in dict_data.items():
#     if val > 1:
#         print(f'{key} - {val}')
#         flag = True
#
# if not flag:
#     print("Однофамильцев нет")
