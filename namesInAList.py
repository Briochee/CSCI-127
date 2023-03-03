#Name: Rio Simpson
#Email: simpson.rions@gmail.com
#Date: 02-28-2023
#Program Description: this program takes names from a list and prints them

nameList = input("Please enter a list of names sperated by a semicolon (;): ")
nameList = nameList.split(";")

for name in nameList:
    nameSplit = name.split(" ")
    print(nameSplit[0], nameSplit[1][0] + ".")
