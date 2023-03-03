#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date: 02-27-2023
#Program Description: this program reverses a string and prints each character twice

newMessage = input("Enter a message: ")
newMessage = newMessage[::-1]

for i in newMessage:
    print(i, i)
