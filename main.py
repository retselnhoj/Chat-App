# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

letSmallPizza = 15
letMediumPizza = 20
letLargePizza = 25
letPepperoniforSmall = 2
letPepperoniforMedium = 3
letPepperoniforLarge = 3
letCheese = 1
if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${letSmallPizza + letPepperoniforSmall + letCheese}.")
    if add_pepperoni == 'Y':
        if extra_cheese == 'N':
            print(f"Your final bill is: ${letSmallPizza + letPepperoniforSmall}.")
    if add_pepperoni == 'N':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${letSmallPizza + letCheese}.")
    if add_pepperoni == 'N':
        if extra_cheese == 'N':
            print(f"Your final bill is: ${letSmallPizza}.")
elif size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${letMediumPizza + letPepperoniforMedium + letCheese}.")
    if add_pepperoni == 'Y':
        if extra_cheese == 'N':
            print(f"Your final bill is: ${letMediumPizza + letPepperoniforMedium}.")
    if add_pepperoni == 'N':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${letMediumPizza + letCheese}.")
    if add_pepperoni == 'N':
        if extra_cheese == 'N':
            print(f"Your final bill is: ${letMediumPizza}.")
elif size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${letLargePizza + letPepperoniforLarge + letCheese}.")
    if add_pepperoni == 'Y':
        if extra_cheese == 'N':
            print(f"Your final bill is: ${letLargePizza + letPepperoniforLarge}.")
    if add_pepperoni == 'N':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${letLargePizza + letCheese}.")
    if add_pepperoni == 'N':
        if extra_cheese == 'N':
            print(f"Your final bill is: ${letLargePizza}.")