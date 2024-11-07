import datetime as dt
import time

tid1 = dt.datetime.now()

print(tid1)

time.sleep(1)

tid2 = dt.datetime.now()

print(tid2)

# Differeanse mellom tider
t_diff = tid2 - tid1
print(t_diff)

# Typene til tidsobjektene
print(f"typen til datetime.now() {type(tid1)}")
print(f"typen til differanse {type(t_diff)}")

print(f"Tidsdifferanse er {t_diff.days} dager og {t_diff.seconds} s og {t_diff.microseconds} mikrosekunder")

# Lage et manuelt tidsobjekt
tid3 = dt.datetime(1983,5,17,1,37)

t_diff_2 = tid1 - tid3
print(f"Tidsdifferanse er {t_diff_2.days} dager")
print(f"Tidsdifferanse er {t_diff_2.days*24*3600:.3e} s")