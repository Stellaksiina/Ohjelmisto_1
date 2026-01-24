import random
N = int(input("How many points will we generate?: "))

n = 0
i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n+=1
    i+=1
pi_likiarvo = 4 * n / N
print("Approximation of pi:", pi_likiarvo)


