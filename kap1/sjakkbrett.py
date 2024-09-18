brett = []
m = 8
n = 8
partall = False
for i in range(m):
    brett.append([])
    for j in range(n):
        if j % 2 == 0 and partall:
            brett[i].append("H")
        else:
            brett[i].append("S")
    partall = not partall

for rad in brett:
    print(rad)
