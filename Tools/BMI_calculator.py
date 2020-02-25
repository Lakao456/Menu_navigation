print("Enter your weight and height with units",
      "Acceptable units of weight--'Kg' and 'lbs'",
      "Acceptable units of weight--'m', 'in' and 'ft'",
      sep="\n", end="\n--------------\n")
flag = False

while flag == False:
    weight = [p for p in input("Enter your weight(kg/lbs)::").split()]
    if len(weight) == 2:
        flag = True
    elif len(weight) == 1:
        print("Please Enter the Units.")
height = [p for p in input("Enter your height(m/in)::").split()]

magnitude_weight = float(weight[0])
magnitude_height = float(height[0])

if "lbs" in weight[1].lower():
    magnitude_weight /= 2.205
if "in" in height[1].lower():
    magnitude_height /= 39.37
if "ft" in height[1].lower():
    magnitude_height /= 3.281

bmi = magnitude_weight / (magnitude_height ** 2)

print("Your BMI is ", bmi)
if bmi < 18.5:
    print("Your are UNDER WEIGHT")
if 24.9 > bmi > 18.5:
    print("Your are HEALTHY")
if bmi > 25:
    print("Your are OBESE")

end = input("Press enter to exit.")
