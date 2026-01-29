import random

nopat = []
noppa_maara = int(input("How many dice to roll: "))
for _ in range(noppa_maara):
    nopat.append(random.randint(1, 6))
if noppa_maara == 1:
    print("Sum of dice: ", sum(nopat))
else:
    print("Sum of the dice: ", sum(nopat))



