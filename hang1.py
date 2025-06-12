import random

words = ["paper","car","tree","ketan"]

chose_word = random.choice(words)
print(chose_word)

place_holder = " "
word_length = len(chose_word)
for position in range (1, word_length + 1):
    place_holder += "_"
print(place_holder)

guess = input("enter a letter\n").lower()

display = ""

for letter in chose_word:
    if letter == guess:
        display += letter
    else:  
        display += "_"
 
print(display)

while "_"in display:
    guess = input("guess a letter\n").lower()
    display = ""
    for letter in chose_word:
        if letter == guess:
            display += letter
        else:  
            display += "_"
    print(display)
print("you win")