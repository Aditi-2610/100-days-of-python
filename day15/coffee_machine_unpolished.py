MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#TODO 4. Check resources sufficient?
def check_resources_sufficient( user_order, order_req):
    if user_order == "latte" or order == "cappuccino":
        if resources["milk"] < order_req["milk"]:
            return "Sorry, there is not enough water."

    if resources["water"] < order_req["water"]:
        return "Sorry, there is not enough milk."
    elif resources["coffee"] < order_req["coffee"]:
        return "Sorry, there is not enough coffee."

    else:
        return ""

#TODO 5. Process coins.

def process_coins(c_pennies, c_nickles, c_dimes, c_quarters):
    total_money = (c_pennies*0.01) + (c_nickles*0.05) + (c_dimes*0.1) + (c_quarters*0.25)
    return total_money


def print_report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")

# TODO 7. Make Coffee.
def make_coffee(user_order, order_detail):
    if user_order == "latte" or order == "cappuccino":
        resources["milk"] -= order_detail["milk"]
    resources["water"] -= order_detail["water"]
    resources["coffee"] -= order_detail["coffee"]
    print("Here is your coffee. Enjoy!")


quarters = 0
dimes = 0
nickles = 0
pennies = 0
print("☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
order = input("What would you like? (espresso/latte/cappuccino):").lower()


#TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
coffee_machine_on = True
while coffee_machine_on:

    if order == "report":
        print_report()
    else:
        order_details = MENU.get(order)
        check_resources_sufficient(order, order_details["ingredients"])
        print("Please insert coins.")
        quarters = int(input("How many quarters:"))
        dimes = int(input("How many dimes:"))
        nickles = int(input("How many nickles:"))
        pennies = int(input("How many pennies:"))

        # TODO 6. Check transaction successful?
        money_received = process_coins(pennies, nickles, dimes, quarters)
        if order_details["cost"] > money_received:
            print("Sorry that's not enough money. Money refunded.")
        elif order_details["cost"] < money_received:
            change_returned = money_received - order_details["cost"]
            print(f"Here is {change_returned:.2f} dollars in change")
            make_coffee(order, order_details["ingredients"])

        else:
            make_coffee(order, order_details["ingredients"])




    #TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    print("☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "off":
        coffee_machine_on = False
#TODO 3. Print report.










