#Name: Rio
#Email:
#Date: Feburary 21st, 2023
#This program takes a user's input as a string and outputs it in 3 different forms

userMessage = input("Enter Three Words Seperated by comma (,):")
userMessage = userMessage.split(", ")
userMessageReverse = userMessage[::-1]
userMessageJoin = " "
userMessageReverseStr = userMessageJoin.join(userMessageReverse)

print("New Phrase:", userMessageReverseStr)
print("Lower Message:", userMessageReverseStr.lower())
print("Upper Message", userMessageReverseStr.upper())
