#Name: Rio
#Email:
#Date: 02-28-2023
#Program Description: converts gallongs to litres and vice versa

print("(a) Convert Gallons to Litres\n(b) Convert Litres to Gallons")
choice = input("Enter a or b: ")

if choice != "a" and choice != "b":
    print("Please only enter a or b")
    choice = input("Wrong Choice, Please enter only a or b: ")

if choice == "a":
    gal = float(input("Enter number of gallon(s): "))
    litrConvert = gal * 3.79
    litrConvert = round(litrConvert, 2)
    print(gal, "gallon(s) =", litrConvert, "litre(s)")
if choice == "b":
    litr = float(input("Enter number of litre(s): "))
    galConvert = litr * 0.26
    galConvert = round(galConvert, 4)
    print(litr, "litre(s) =", galConvert, "gallon(s)")

