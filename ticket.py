print("welcome to roller coster")
h = float(input("enter your height \n"))
bill = 0


if h >= 120:
    print("welcome")
    age = int(input("enter age = \n"))
    if age <=12:
        bill = 12
        print("tickit is 5 ")
    elif age <= 15:
        bill = 10
        print("ticket is 10 ")
    elif age >= 45 and age <= 50:
            bill = 0
            print("your bill is null")    
        
    else:
        bill = 15
        print("tickit is 15 ")
        
        
        want_photo = input("want photo y for yes n for no '\n")
        if want_photo == "y":
            bill += 3
            print(f"final bill ={bill}")
else:
    print("go home")
