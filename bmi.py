weight = float(input("w"))
height = float(input("h"))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi >= 25:
    print("underweight")
elif bmi >= 18.5 :
    print("normal weight")
else:
    print("overweight")