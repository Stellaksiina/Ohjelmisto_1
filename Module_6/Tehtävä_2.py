import random
nopan_sivut = int(input("Kuinka monta sivua nopassa?: "))
noppa = 0
def roll_dice(nopan_sivut):
    noppa = random.randint(1, nopan_sivut)
    while noppa != nopan_sivut:
        print(noppa)
        noppa = random.randint(1,nopan_sivut)
    else:
        print(noppa)

roll_dice(nopan_sivut)
