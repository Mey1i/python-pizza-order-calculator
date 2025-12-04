print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ").upper()
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size! Please enter S, M or L.")
    exit()

pepperoni = input("Do you want pepperoni? Y or N: ").upper()
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
elif pepperoni != "N":
    print("Invalid choice! Please enter Y or N.")
    exit()

extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == "Y":
    bill += 1
elif extra_cheese != "N":
    print("Invalid choice! Please enter Y or N.")
    exit()

print(f"Thank you for ordering the pizza! Your final bill is ${bill}")
