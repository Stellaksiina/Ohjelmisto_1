import random
noppa = 0
def roll_dice():
    noppa = random.randint(1, 6)
    while noppa != 6:
        print(noppa)
        noppa = random.randint(1,6)
    else:
        print(noppa)

roll_dice()
