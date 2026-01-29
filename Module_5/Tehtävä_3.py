num = int(input("Enter an integer: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    on_alkuluku = True
    for i in range(2, num):
        if num % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number")