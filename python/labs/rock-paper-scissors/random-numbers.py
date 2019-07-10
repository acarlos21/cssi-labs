import random

print("Welcome to Anthony's dice")
die1 = random.randint(1,6)
die2 = random.randint(1,6)

sum = die1 + die2
# print(sum)
if die1 == die2:
    print("You rolled a double %s's Roll again"%(die1))
else:
    print("You roll a %s now its the next player's turn"%(sum))
