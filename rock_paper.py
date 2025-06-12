import random


rock ='''
     ______     
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          

    '''
paper ='''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

          
          '''
scisor = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          

'''

game_image = [rock,paper,scisor]
user = int(input("enter your move = "))
if user >= 0 and user <= 2:
    print(game_image[user])

computer_choise = random.randint(0,2)
print("computer_choise")
print(game_image[computer_choise])

if user >= 3 or user < 0:
    print("invalid input you lose")
elif user == 0 and computer_choise == 2:
    print("user wins")
elif computer_choise == 0 and user == 2:
    print("computer win")    
elif computer_choise > user:
    print("computer wins")
elif user > computer_choise:
    print("user wins")    
elif user == computer_choise:
    print("its draw")

1