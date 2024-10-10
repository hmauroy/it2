l = ["Asterix"]

try:
    l.remove("asteriX".capitalize())
    print("Fjernet asteriX")
except ValueError:
    print("Finnes ikke")