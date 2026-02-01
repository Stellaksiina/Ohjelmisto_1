import math
def calculate_unit_price(diameter_cm, price_euro):
    pizza_radius = (diameter_cm/2) / 100
    area = math.pi*pizza_radius**2
    pizza_unit_price = price_euro / area
    return pizza_unit_price



diameter_eka = float(input("Enter the diameter of the first pizza (cm): " ))
price_eka = float(input("Enter the price of the first pizza (euros): "))

diameter_toka = float(input("Enter the diameter of the second pizza (cm): " ))
price_toka = float(input("Enter the price of the second pizza (euros): "))

pizza_unit_price1 = calculate_unit_price(diameter_eka, price_eka)
pizza_unit_price2 = calculate_unit_price(diameter_toka, price_toka)

print(f"Unit price of the first pizza: {pizza_unit_price1:.2f} euros/m²")
print(f"Unit price of the second pizza: {pizza_unit_price2:.2f} euros/m²")

if pizza_unit_price1 < pizza_unit_price2:
    print("The first pizza provides better value for money.")
elif pizza_unit_price2 < pizza_unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide equal value for money.")