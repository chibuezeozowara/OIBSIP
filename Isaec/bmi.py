height = float(input("what is your height in m: "))
weight = float(input("what is your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi > 18.5 < 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi > 25 < 30:
    print(f"Your bmi is {bmi}, you are over weight")
elif bmi > 30 < 35:
    print(f"Your is bmi is {bmi}, you are slightly obese")
else:
    print(f"Your is bmi is {bmi}, you are clinically obese")