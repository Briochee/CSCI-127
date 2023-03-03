myString = "hello its me"
print(myString [::2])

print("\ncontents of range (1, 5, 2):") #\n is new line character
for i in range (1, 5, 2): #starts from 1, ends before 5,intervals of 2
    print(i)

string = "hello, world"
#print each letter of the string, in one line
print("print each letter of the string on its own line")
for ch in (string):
    print(ch)

print("\nprint each letter in string, on one line, using character at string")
size = len(string)
for i in range(size):
    print(string[i])

print("\nprint the first five letters of string")
print(string[0:5])

print(string [0:5:2]) #prints the first 5 letters with intervals of 2

s = "FridaysSaturdaysSundays"
num = s.count('s') #what happens if we use num -- it counts the number of instances
print("there are", num, "fun days in a week.")

days = s[:-1].split('s') # what is s[:-1]? -- removes lowercase 's'
mess = days[0]
print("Two of them are", mess, days[-1]) #this prints the days minus sunday

result = " "
for i in range(len(mess)): #what is len(mess) -- mess=day[0] which is the day in position 0, which is friday
                            #len(mess) is the length of that string, friday has length 6
                            #this becomes for i in range(6)
    if i>2: #6 is more than 2 positions 0,1,2 are omitted from the string "friday" -- leaving day
        result = result + mess[i] #result becomes "day" since mess = friday, i is index of greater than 2 in range 6
print("my favorite", result, "is saturday")


daysList = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

size = len(daysList) #find out number of elements in dayList
for i in range(size):
    print(daysList[i], end=" ")
    #end=" " means printed items are sperated by a space


