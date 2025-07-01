import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
Number = ['0','1','2','3','4','5','6','7','8','9']
Symbol = ['!','@','#','$','%','^','&','*','(',')']


nr_Letters = int(input("enter number of Letters \n"))
nr_Number = int(input("enter number of Numbers \n"))
nr_Symbol = int(input("enter number of Symbols \n "))

#passsword = ""
#for char in range(0, nr_Letters):
#    password += random.choice(Letters)
#
#for char in range(0, nr_Letters):
#    password += random.choice(numbers)
#
#for char in range(0, nr_Letters):
#    password += random.choice(symbols)
#
#print(password) 
#
password = []

for char in range(0, nr_Letters):
    password.append(random.choice(Letters))
  
for char in range (0,nr_Number):
    password.append(random.choice(Number))

for char in range (0,nr_Symbol):
    password.append(random.choice(Symbol))

print(password)    
random.shuffle(password)
print(password)

password = "".join(password)
print("this is your password: ",password)
