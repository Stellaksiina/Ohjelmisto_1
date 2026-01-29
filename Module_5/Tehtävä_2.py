numbers = []
number = 0

while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers.append(float(number))

numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")

kerrat = 0

for i in numbers:
    if kerrat < 5 :
        print(i)
        kerrat += 1



