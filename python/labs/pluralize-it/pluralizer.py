print("Welcome to Anthony's Pluralizer!")
word1 =raw_input("Give me a word: ")
number1 =int(raw_input("Give me a number: "))


if number1 == 1:
    print(str(number1) + " "+word1)
elif number1 == 0:
    print(str(number1) + " "+word1 + "s")
else:
    print(str(number1) + " "+word1 + "s")
