import random
Totolec = random.sample(range(1,61),6)
Totolec.sort()
for c in range(0,6):
    print(f"numero[{c + 1}]: {Totolec[c]}")

