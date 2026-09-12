weight = int(input("Enter your weight: "))
units = input("Is your weight in lbs or kg?: ").lower()
if units == "kg":
    weight_lbs = weight * 2.20462
    print(f"Your weight is {weight_lbs} Lbs")
elif units == "lbs":
       weight_kg = weight * 0.453592
       print(f"Your weight is {weight_kg} Kg")


