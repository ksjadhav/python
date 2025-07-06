# Missing closing parenthesis in the print statement
print("This line of code is before both IF-ELSE functions")  

countervariable = 125

# Error: Misspelled variable name 'countervarable'. Should be 'countervariable'.
if countervariable < 100:  
    print("Counter is smaller than 100")
    print("This line is in the first if section")
else:
    # Error: Missing colon (:) after 'else'. Colon is required to define the block.
    print("Counter is greater than 100")
    print("This line is in the first else section")

number = 3

# Error: Missing closing quotation mark for the string in print statement.
if number > 0:  
    print("Number is a positive number")  # Corrected missing closing quotation mark
    print("This line is in the second if section")
else:
    print("Number is a negative number")
    print("This line is in the second else section")

print("This line of code is after both of the IF-ELSE functions")
