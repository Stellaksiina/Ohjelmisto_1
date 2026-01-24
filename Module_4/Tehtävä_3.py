numbers = []
while True:
    syote = input("Enter a number (or press Enter to quit): ")

    if syote == "":
        break

    num = float(syote)
    numbers.append(num)

numbers.sort()

if numbers:
    print(f"Smallest number: {numbers[0]}")
    print(f"Largest number: {numbers[-1]}")

