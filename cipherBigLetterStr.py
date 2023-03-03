#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date:02-21-2023
#Program Description: This program shifts the chracters of an inputted phrase

phraseInput = input("Enter an all-big-letter string:")
intInput = input("Enter a non-negative int to shift:")
intInput = int(intInput)

cipheredString = " "

for i in phraseInput:
    offset = ord(i) - ord("A")
    encrypt = (offset + intInput) % 26
    newchrs = chr(ord("A") + encrypt)
    cipheredString = cipheredString + newchrs

print("After shifting", intInput, "letters,", phraseInput, "becomes", cipheredString)
    
