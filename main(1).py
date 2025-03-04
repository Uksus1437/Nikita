q = [i for i in range(3, 10000, 3)]
p = [i for i in range(5, 10000, 5)]

for kr in range(2, 30):
    a = [i for i in range(kr, 10000, kr)]
    fl = True
    for x in range(1, 10000):
        if ( (x in q) <= ((x in p) <= (x in q) and (x in a)) ) == 0:
            fl = False
            break
    if fl == True:
        print(kr)