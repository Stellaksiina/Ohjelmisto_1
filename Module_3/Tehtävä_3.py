gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gender == "female" and hemoglobin < 117 or gender == "male" and hemoglobin < 134:
    print("Your hemoglobin is low.")
elif gender == "female" and hemoglobin > 155 or gender == "male" and hemoglobin > 167:
    print("Your hemoglobin is high.")
elif gender == "female" and 117 <= hemoglobin <= 155 or gender == "male" and 134 <= hemoglobin <= 167:
    print("Your hemoglobin is normal.")
else:
    print("Invalid gender.")