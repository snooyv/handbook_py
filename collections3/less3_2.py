# D Кашееды /////////

semol_porrg_vol = int(input())
oatml_porrg_vol = int(input())

sem_porr_licke_name = []
oat_porr_licke_name = []

for i in range(semol_porrg_vol):
    sem_porr_licke_name.append(input())

for i in range(oatml_porrg_vol):
    oat_porr_licke_name.append(input())

result = set(sem_porr_licke_name) & set(oat_porr_licke_name)

print(len(result)) if len(result) else print("Таких нет")