# A Азбука ///////////

vol_word = int(input())

is_has = "YES"

while vol_word > 0:
    data = input()

    vol_word -= 1
    if is_has == "NO":
        continue
    if not data.startswith("а") and not data.startswith("б") and not data.startswith("в"):
        is_has = "NO"

print(is_has)
