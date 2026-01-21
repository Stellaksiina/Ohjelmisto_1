zander = float(input("Enter the length of the zander in centimeters: "))
puuttuvat_sentit = 42-zander
if zander < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {puuttuvat_sentit:.1f} centimeters below the size limit.")

if zander >= 42:
    print("The zander meets the size limit.")