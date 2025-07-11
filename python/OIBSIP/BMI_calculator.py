weight= float(input("Enter your weight in kgs:"))
height= float(input("Enter your height in meters:"))
age= int(input("Enter your age in years:"))

bmi= weight/height**2
print("your BMI in kg per meter sq is :", bmi)

if bmi<16:
    print("Severe Thinness")
elif (bmi >= 16) and (bmi < 17):
    print("Moderate Thinness")
elif (bmi >= 17) and (bmi<18.5):
    print("Mild Thinness")
elif (bmi >= 18.5) and (bmi < 25):
    print("Normal")
elif (bmi >= 25) and (bmi<30):
    print("Overweight")
elif (bmi >= 30) and (bmi < 35):
    print("Obese class 1")
elif (bmi >= 35) and (bmi<40):
    print("Obese class 2")
else:
    print("Obese class 3")
 
 










