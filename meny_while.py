"""
Menysystem.
"""
isRunning = True
while isRunning:
    print("Meny")
    for i in range(1,5):
        print(f"{i} - Meny {i}")
    print("0 - Avslutt")
    valg = int(input("Menyvalg: "))
    if valg == 0:
        bekreft = input("Er du sikker? [y,n]: ")
        if bekreft == "y":
            isRunning = False
    else:
        print(f"Du valgte {valg}")
