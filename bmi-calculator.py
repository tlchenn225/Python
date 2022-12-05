# ask height and weight from user to calculate BMI
height_cm = float(input("Enter your height (cm): "))
weight_kg = float(input("Enter your weight (kg): "))

# convert height units cm to m
height = height_cm/100

# calculate BMI
BMI = weight_kg/(height**2)

# Determine what BMI based on input
if BMI < 18.5:
    print("Your BMI is ",BMI ,"- BMI category is underweight")
elif BMI >= 18.5 or BMI <= 24.9:
    print("Your BMI is",BMI ,"- BMI category is normal")
elif BMI >= 25 or BMI <= 29.9:
    print("Your BMI is",BMI ,"- BMI category is overweight")
elif BMI >= 30:
    print("Your BMI is", BMI, "- BMI category is obese")




