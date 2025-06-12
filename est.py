print("welcome to python pizza ")
size = input("enter size s,m and l")
pepperoni = input("you want pepperoni")
chees = input("you want chees")

bill = 0

if size == "s":
    bill += 20
    
elif size == "m":
    bill += 25
    
elif size == "l":
    bill += 30

else:
    print("wrong input")
        
if pepperoni == "y":
    if size == "s":
        bill += 10
    else:
        bill +=15
    
if chees == "y":
    bill += 10
print(f"final bill is: {bill}.")
