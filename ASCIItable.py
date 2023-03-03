#Name: Rio
#Email:
#Date: Feburary 21st, 2023
#Program Description:this program gives the ASCII code for a input term and two letters before it

userInput = input("Enter a phrase: ")

print("letter ASCII two_letter_before")

for i in userInput:
    print("%6c %5i %17c"%(i, ord(i), chr(ord(i)-2)))
