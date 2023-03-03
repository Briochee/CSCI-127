#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date: Feburary 21st, 2023
#This program takes a user's input as a string and outputs it in 3 different forms

userInput = input("Enter three words seperated by comma (,):")

newString = userInput.split(",")
newStringReverse = newString.reverse()
space = " "
joinString = space.join(newString)

print("new string:", joinString)
print("lower string:", joinString.lower())
print("upper string:", joinString.upper())
