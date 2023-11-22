# ClydeBank Coffeeshop Simulator 4000
# Copyright (C) 2023 ClydeBank Media, All Rights Reserved

# Import items from the random module to generate weather

from random import seed
from random import randint


#Current day number
day = 1

# Starting cash on hand
cash = 100.00

# Coffee on hand (cups)

coffee = 100

#Sales list of dictionaries
sale = [
    {
        "day": 1,
        "coffee_inv": 100,
        "advertising": "10",
        "temp": 68,
        "cups_sold": 16
    },
    {
        "day": 2,
        "coffee_inv": 84,
        "advertising": "15",
        "temp": 72,
        "cups_sold": 20
    },
    {
        "day": 3,
        "coffee_inv": 64,
        "advertising": "5",
        "temp": 78,
        "cups_sold": 10
    },
]
#Create an emoty sales list
sales = []

# Print welcome message

print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
print("Copyright (C) 2023 ClydeBank Media, All Rights Reserved")
print("Let's collect ome information before we start the game.\n")

# Get name and shop name using the following approach.
# set name and shop_name to False.
# Use while not name and shop_name to continue to prompt for a non-empty string.

name = False
while not name:
    name = input("What is your name?")

shop_name = False
while not shop_name:
    shop_name = input("What do you want to name your coffee shop? ")

# We have what we need, so let's get started.     

print("\nOK, let's get started. Have fun!")

# The main game loop

running = True
while running:
    # Display the day and add a "fancy" text effect
    print("\n-----| Day " + str(day) + " @ " + shop_name + " |-----")

    # Generate a random temperature between 20 and 90
    # We'll consider seasons later on
    temperature = randint(10,90)

    # display the cash and weather
    print("You have $" + str(cash) + " cash and it's " + str(temperature) + " degrees.")
    print("You have coffee on hand to make " + str(coffee) + " cups.\n")

    # Get price for a cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")

    # Determine advertising spend
    print("\nYou can buy advertising to help promote sales.")
    advertising = input("How much advertising do you want to buy (0 for none)?")

    # Convert advertising into a float
    advertising = float(advertising)

    # Deduct advertising from cash on hand
    cash -= advertising

    # TODO: calculate today's performance
    # TODO: display today's performance

    # Before we loo paround, add a day
    day += 1





# Display what we have
print("\nGreat. Here's what we've collcted so far. \n")
print("Your name is " + name + " and you're opening " + shop_name + "!")
print("Your first cup of coffee will sell for $" + cup_price + ".\n")
