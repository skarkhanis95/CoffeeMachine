from data import resources
from data import MENU
from os import system, name
import time


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_resources():
    for resource in resources:
        if resource == 'water' or resource == 'milk':
            print(f"{resource.title()}: {resources[resource]}ml")
        if resource == 'coffee':
            print(f"{resource.title()}: {resources[resource]}g")
        if resource == 'money':
            print(f"{resource.title()}: ${resources[resource]}")
    if not "money" in resources:
        resources["money"] = 0.0
        print(f"Money: $0.0")


def check_resources(flavour):
    if flavour == 'espresso':
        required_qtys = MENU[flavour]["ingredients"]
        if resources["water"] < required_qtys["water"]:
            return "Not Sufficient Water"
        elif resources["coffee"] < required_qtys["coffee"]:
            return "Not Sufficient Coffee"
        else:
            return "True"
    elif flavour == 'latte' or flavour == 'cappuccino':
        required_qtys = MENU[flavour]["ingredients"]
        if resources["water"] < required_qtys["water"]:
            return "Not Sufficient Water"
        elif resources["coffee"] < required_qtys["coffee"]:
            return "Not Sufficient Coffee"
        elif resources["milk"] < required_qtys["milk"]:
            return "Not Sufficient Milk"
        else:
            return "True"


def process_coins(q, d, n, p):
    QUARTERS = 0.25
    DIMES = 0.10
    NICKLES = 0.05
    PENNIES = 0.01
    q = q*QUARTERS
    d = d*DIMES
    n = n*NICKLES
    p = p*PENNIES
    total_amount = q + d + n + p
    return total_amount


def calculate_amount(amount_paid, flavour):
    cost = MENU[flavour]["cost"]
    if amount_paid == cost:
        return 0
    elif amount_paid > cost:
        return round(amount_paid-cost,2)
    elif amount_paid < cost:
        return amount_paid - cost


def deduct_resources(flavour):
    required_qtys = MENU[flavour]["ingredients"]
    if flavour == 'espresso':
        resources["water"] -= required_qtys["water"]
        resources["coffee"] -= required_qtys["coffee"]
    else:
        resources["water"] -= required_qtys["water"]
        resources["coffee"] -= required_qtys["coffee"]
        resources["milk"] -= required_qtys["milk"]





def coffee_machine():
    turn_on_coffee_machine = True
    while turn_on_coffee_machine:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            available = check_resources(user_choice)
            if available == "True":
                print("Please Insert Coins")
                q = int(input("How many Quarters?: "))
                d = int(input("How many Dimes?: "))
                n = int(input("How many Nickles?: "))
                p = int(input("How many Pennies?: "))
                total_amount = process_coins(q,d,n,p)
                change = calculate_amount(total_amount,user_choice)
                if change >=0:
                    print(f"Here is your change: ${change}")
                    profit = round(total_amount - change, 2)
                    if not "money" in resources:
                        resources["money"] = 0.0
                    resources["money"] += profit
                    deduct_resources(user_choice)
                    print("Making Coffee.......")
                    time.sleep(3.0)
                    print(f"Here is you're fresh cup of {user_choice.title()}")
                    time.sleep(2.0)
                    #clear()
                else:
                    print(f"You have paid less amount for {user_choice.title()}")
                    print(f"Here is your money back: ${round(total_amount,2)}")
            else:
                print(available)
        elif user_choice == 'report':
            print_resources()
        elif user_choice == 'off':
            turn_on_coffee_machine = False
        else:
            print(f"Sorry we don't have {user_choice.title()} yet. Please try again with available options.")
            coffee_machine()


coffee_machine()

