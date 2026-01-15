talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
lots1 = lots*13.3
pounds1 = pounds*32*13.3
talents1 = talents*20*32*13.3
total_grams = lots1+pounds1+talents1
kilograms = int(total_grams//1000)
remaining_grams = total_grams-kilograms*1000
print(f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")

# talents_str = input("Enter talents: ")
# pounds_str = input("Enter pounds: ")
# lots_str = input("Enter lots: ")
#  talents = float(talents_str)
# pounds = float(pounds_str)
# lots = float(lots_str)
# lots1 = lots*13.3
# pounds1 = pounds*32*13.3
# talents1 = talents*20*32*13.3
# total_grams = lots1+pounds1+talents1
# kilograms = total_grams
# remaining_grams = total_grams-kilograms
# print("The weight in modern units: " + str(kilograms.real) + " grams")
