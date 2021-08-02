# A simple python project for multiple users
import datetime
import getpass
import accounts

now = datetime.datetime.now()

# list of users, pin, balance


def changePin():
    current_pin = getpass.getpass("enter your current")
    if current_pin != accounts.atmDetails[user]["pin"]:
        print("You have entered wrong pin")
        exit()
    else:
        newPin = getpass.getpass("enter the new pin")
        newPin2 = getpass.getpass("re-enter new pin")
        if newPin == newPin2:
            print("pin changed successfully")
        else:
            print("pin do not match")
            changePin()


def depositFunds():
    amount = input("Enter the amount you would like to deposit: ")
    amount = float(amount)

    bal = accounts.atmDetails[user]["balance"]["KES"]

    bal = float(bal) + amount

    accounts.atmDetails[user]["balance"].update({"KES": bal})

    usd = bal * 107.75

    accounts.atmDetails[user]["balance"].update({"USD": usd})
    print("The new balance is KES{}\n".format(bal))

    receipt = input(f'Would you like a receipt? (Type yes or no): ')
    if receipt == "yes":
        print("Thank you for the transaction. Welcome again")
        choice3 = input("Would you like to perform another transaction? (Type yes or no): ")

        if choice3 == "yes":
            serviceSelection()
        elif choice3 == "no":
            print("Thank you for your visit. Welcome again")
            exit()
        else:
            print("Invalid choice")
            exit()
    elif receipt == "no":
        x = input("Would you like to perform another transaction? (Type yes or no): ")
        if x == "yes":
            serviceSelection()
        else:
            exit()
    else:
        print("Invalid choice")
        exit()


def withdrawFunds():
    amount = input("Enter the amount you would like to withdraw: ")
    amount = float(amount)

    bal = accounts.atmDetails[user]["balance"]["KES"]

    bal = float(bal) - amount

    if bal < 0:
        print("You have insufficient funds")
        withdrawTrials = input('Would you like to try again? (Type yes or no): ')
        if withdrawTrials == "yes":
            withdrawFunds()
        else:
            accounts.atmDetails[user]["balance"].update({"KES": bal})

            usd = bal * 107.75

            accounts.atmDetails[user]["balance"].update({"USD": usd})

            choice2 = input("Would you like to perform another transaction? (Type yes or no): ")
            if choice2 == "yes":
                serviceSelection()
            elif choice2 == "no":
                print("Thank you for your visit. Welcome again")
                exit()
            else:
                print("Invalid choice")
                exit()

    print("The new balance is KES.{}\n".format(bal))
    receipt = input(f'Would you like a receipt? (Type yes or no): ')
    if receipt == "yes":
        print("Thank you for the transaction. Welcome again")
        choice3 = input("Would you like to perform another transaction? (Type yes or no): ")

        if choice3 == "yes":
            serviceSelection()
        elif choice3 == "no":
            print("Thank you for your visit. Welcome again")
            exit()
        else:
            print("Invalid choice")
            exit()
    elif receipt == "no":
        x = input("Would you like to perform another transaction? (Type yes or no): ")
        if x == "yes":
            serviceSelection()
        else:
            exit()
    else:
        print("invalid choice")
        exit()


def serviceSelection():
    print("Which service would you like to access? \n1. Cash Deposit\n2. Cash Withdrawal\n3. Change pin\n4.exit")
    choice = input("Enter your selection here: ")

    if choice == "1":
        depositFunds()

    elif choice == "2":
        withdrawFunds()
    elif choice == "3":
        changePin()
    elif choice == "4":
        print("Thank you for your visit. Welcome again")
        exit()
    else:
        print("Invalid choice.")


# while loop chaecks if a name is among the users
print("#*#*#*M*#A*#S*#H*#I*#N*#A*#N*#I*#B*#A*#N*#K#*#*")
print("       WELCOME TO MASHINANI BANK       ")
print("Today is on:")
print(str(now))
print("#*#*#*M*#A*#S*#H*#I*#N*#A*#N*#I*#*#*#*#*#*#*#*#*")

user = input('\nENTER USER NAME: ')
user = user.lower()
if user not in accounts.atmDetails:

    print('----------------')
    print('****************')
    print('INVALID USERNAME')
    print('****************')
    print('----------------')
else:
    print('------------------')
    print('******************')
    pin = getpass.getpass('PLEASE ENTER PIN: ')
    print('******************')
    print('------------------')
    if accounts.atmDetails[user]["pin"] != pin:
        count = 1
        while count < 3:
            print('------------------')
            print('******************')
            pin = getpass.getpass(' INVALID PIN! PLEASE ENTER PIN: ')
            print('******************')
            print('------------------')
            count += 1

        if count == 3:
            print('TOO MANY ATTEMPTS TRY AGAIN LATER!')
    else:
        print("Login Successful.")
        serviceSelection()


def depositFunds():
    amount = input("Enter the amount you would like to deposit: ")
    amount = float(amount)

    bal = accounts.atmDetails[user]["balance"]["KES"]

    bal = float(bal) + amount

    accounts.atmDetails[user]["balance"].update({"KES": bal})

    usd = bal * 107.75

    accounts.atmDetails[user]["balance"].update({"USD": usd})
    print("The new balance is KES{}\n".format(bal))

    receipt = input(f'Would you like a receipt? (Type yes or no): ')
    if receipt == "yes":
        print("Thank you for the transaction. Welcome again")
        choice3 = input("Would you like to perform another transaction? (Type yes or no): ")

        if choice3 == "yes":
            serviceSelection()
        elif choice3 == "no":
            print("Thank you for your visit. Welcome again")
            exit()
        else:
            print("Invalid choice")
            exit()
    elif receipt == "no":
        x = input("Would you like to perform another transaction? (Type yes or no): ")
        if x == "yes":
            serviceSelection()
        else:
            exit()
    else:
        print("Invalid choice")
        exit()


def withdrawFunds():
    amount = input("Enter the amount you would like to withdraw: ")
    amount = float(amount)

    bal = accounts.atmDetails[user]["balance"]["KES"]

    bal = float(bal) - amount

    if bal < 0:
        print("You have insufficient funds")
        withdrawTrials = input('Would you like to try again? (Type yes or no): ')
        if withdrawTrials == "yes":
            withdrawFunds()
        else:
            accounts.atmDetails[user]["balance"].update({"KES": bal})

            usd = bal * 107.75

            accounts.atmDetails[user]["balance"].update({"USD": usd})

            choice2 = input("Would you like to perform another transaction? (Type yes or no): ")
            if choice2 == "yes":
                serviceSelection()
            elif choice2 == "no":
                print("Thank you for your visit. Welcome again")
                exit()
            else:
                print("Invalid choice")
                exit()

    print("The new balance is KES.{}\n".format(bal))
    receipt = input(f'Would you like a receipt? (Type yes or no): ')
    if receipt == "yes":
        print("Thank you for the transaction. Welcome again")
        choice3 = input("Would you like to perform another transaction? (Type yes or no): ")

        if choice3 == "yes":
            serviceSelection()
        elif choice3 == "no":
            print("Thank you for your visit. Welcome again")
            exit()
        else:
            print("Invalid choice")
            exit()
    elif receipt == "no":
        x = input("Would you like to perform another transaction? (Type yes or no): ")
        if x == "yes":
            serviceSelection()
        else:
            exit()
    else:
        print("invalid choice")
        exit()


'''if passcode.isdigit():
		if user == "solomon":
			if passcode == passcode[0]'''
