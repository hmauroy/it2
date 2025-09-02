
file_path = "kryptert_1_utf8.txt"
#file_path = "kryptert_2_utf8.txt"
#file_path = "kryptert_3_utf8.txt"

with open(file_path, 'r', encoding="utf-8") as file:
    text = file.read()


data = {}

tegn = [".",",","!",":","?"," "]

antall = 0

for c in text:
    if c in tegn:
        continue
    if c in data:
        data[c] += 1
    else:
        data[c] = 1
    antall += 1

for key,val in data.items():
    data[key] = 100*val/antall
    print(key,data[key])