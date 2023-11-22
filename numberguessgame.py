from random import seed
from random import randint

number = randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
input("Can you guess it?")
if input == number:
    print("Good job!")
else:
    print("Nope, sorry, it's " + str(number) + ".")