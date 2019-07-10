print("Welcome to this practice of loops in Python SKSKSKS")

myString = raw_input("Give me a string loop through: ")

#Create a program that will print each letter in teh string individually
#using a for loop
letterNum = 1

for character in myString:
    print("This is letter number %s" % (letterNum))
    letterNum = letterNum + 1
    print(character)
