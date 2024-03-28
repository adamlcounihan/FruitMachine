import time
def start():
    time.sleep(0.25)
    print(" _______________________________  ")
    print("/                               \ ")
    print("|        Welcome to the         | ")
    print("|         Fruit Machine         | ")
    print("|                               | ")
    print("\_______________________________/ ")
    time.sleep(1.25)



    print("")
    print("Answer each question with only 'yes' or 'no'.")
    time.sleep(1.25)
    print("")
    print("Each spin costs 50p. If you run out of money, you lose.")
    time.sleep(1.25)
    print("")
    print("2 of a kind = 50p. 3 a kind = £1. 3 bells = £5.")
    time.sleep(1.25)
    print("")
    print("Roll 2 skulls = loose £1. Roll 3 skulls = lose all money.")
    time.sleep(1.25)
    print("_______________________________________________________________________")
    print("")
    print("")
    credit = float(input("Enter a value of money into the machine (1 = £1, 2.5 = £2.50 etc)"))


    
    while True:
        import random
        wheel = ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
        wheel1 = random.choice(wheel)
        wheel2 = random.choice(wheel)
        wheel3 = random.choice(wheel)


        
        start = input("Would you like to roll the wheels?")
        if start == "no":
            print("Your total winnings are £" + str(credit))
            break
        
        elif start == "yes":
            time.sleep(0.5)
            credit = (credit - 0.50)
            credit = round(credit, 2)
            print("")
            print("**You enter 50p into the machine**")
            print("Total credit now £" + str(credit))
            time.sleep(0.5)
            print("")
            print(" -*****-  Wheels Spinning -*****- ")
            print("")
            print("")
            print("")
            time.sleep(1)
            print(wheel1 + " - " + wheel2 + " - " + wheel3)
            print("")



            #if all three wheels are skulls
            if wheel1 == "Skull" and wheel2 == "Skull" and wheel3 == "Skull":
                print("You have lost all your money!")
                credit = (credit - credit)
                if credit <= 0.1:
                    print("No Credits Remaining....")
                    print("")
                    break

                
            elif (wheel1 == "Skull" and wheel2 == "Skull"
                  or wheel2 == "Skull" and wheel3 == "Skull"
                  or wheel1 == "Skull" and wheel3 == "Skull"):
                
                print("You have lost £1!")
                credit = (credit - 1)
                if credit <= 0.1:
                    print("No Credits Remaining....")
                    print("")
                    break
                
            elif wheel1 == wheel2 == wheel3:
                print("You won £1!")
                credit = (credit + 1)
                if credit <= 0.1:
                    print("No Credits Remaining....")
                    print("")
                    break

                
            elif (wheel1 == wheel2 and wheel1 != "Skull" and wheel1 != wheel3
                  or wheel1 == wheel3 and wheel1 != "Skull" and wheel1 != wheel2
                  or wheel2 == wheel3 and wheel2 != "Skull" and wheel2 != wheel1):
                
                print("Two of a kind!")
                print("You won 50p!")
                credit = (credit + 0.5)
                if credit <= 0.1:
                    print("No Credits Remaining....")
                    print("")
                    break

                
            elif wheel1 == "Bell" and wheel2 == "Bell" and wheel3 == "Bell":
                print("3 Bells! You won £5!")
                credit = (credit + 5)
                if credit <= 0.1:
                    print("No Credits Remaining....")
                    print("")
                    break

                
            elif wheel1 != wheel2 and wheel1 != wheel3 and wheel2 != wheel3:
                print("You got nothing!")
                if credit <= 0.1:
                    print("No Credits Remaining....")
                    print("")
                    break


            credit = round(credit, 2)
            print("Total credits is £" + str(credit))
            print("")

            
        else:
            print("Sorry, I don't understand.")
                

start()
