def gallons_to_liters(bensiinin_maara):
    gallon = float(input("Enter a volume in American gallons (negative value to quit): "))
    while gallon > 0:
        bensiinin_maara = gallon*3.785
        print(f"{gallon} American gallons is {bensiinin_maara:.2f} liters.")
        gallon = float(input("Enter a volume in American gallons (negative value to quit): "))
bensiinin_maara = 0
gallons_to_liters(bensiinin_maara)

print("Program finished.")