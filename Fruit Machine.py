import time
import random

# Constants
COST_PER_SPIN = 0.50
WIN_TWO_KIND = 0.50
WIN_THREE_KIND = 1.00
WIN_BELLS = 5.00
LOSS_SKULLS_TWO = 1.00
LOSS_SKULLS_THREE = 'all'

def print_intro():
    print(" _______________________________  ")
    print("/                               \\ ")
    print("|        Welcome to the         | ")
    print("|         Fruit Machine         | ")
    print("|                               | ")
    print("\\_______________________________/ ")
    print("\nAnswer each question with 'spin' to play or 'quit' to exit.")
    print("Each spin costs £0.50. If you run out of money, you lose.")
    print("2 of a kind = £0.50. 3 a kind = £1. 3 bells = £5.")
    print("Roll 2 skulls = lose £1. Roll 3 skulls = lose all money.")
    print("_______________________________________________________________________\n")

def get_credits():
    while True:
        try:
            credit = float(input("Enter a value of money into the machine (1 = £1, 2.5 = £2.50 etc): "))
            return credit
        except ValueError:
            print("Please enter a valid number.")

def spin_wheels():
    wheel = ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
    return random.choice(wheel), random.choice(wheel), random.choice(wheel)

def update_credits(credit, result):
    if result == LOSS_SKULLS_THREE:
        return 0
    return round(credit + result, 2)

def check_result(wheel1, wheel2, wheel3):
    if wheel1 == wheel2 == wheel3:
        if wheel1 == 'Skull':
            return -LOSS_SKULLS_THREE
        elif wheel1 == 'Bell':
            return WIN_BELLS
        else:
            return WIN_THREE_KIND
    elif wheel1 == 'Skull' and wheel2 == 'Skull' or wheel2 == 'Skull' and wheel3 == 'Skull' or wheel1 == 'Skull' and wheel3 == 'Skull':
        return -LOSS_SKULLS_TWO
    elif wheel1 == wheel2 or wheel2 == wheel3 or wheel1 == wheel3:
        return WIN_TWO_KIND
    return -COST_PER_SPIN

def main():
    print_intro()
    credit = get_credits()

    while credit > 0:
        action = input("Spin the wheels? (spin/quit): ").lower()
        if action == "quit":
            print(f"Your total winnings are £{credit:.2f}")
            break
        elif action == "spin":
            wheel1, wheel2, wheel3 = spin_wheels()
            result = check_result(wheel1, wheel2, wheel3)
            credit = update_credits(credit, result)
            print(f"{wheel1} - {wheel2} - {wheel3}")
            print(f"Total credits: £{credit:.2f}\n")
        else:
            print("Sorry, I don't understand. Please type 'spin' or 'quit'.")

if __name__ == "__main__":
    main()
