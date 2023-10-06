MENU = {
    "esp": {
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
    "cap": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#1 functiom
def complete_hai(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"sorry there is no enough {item}")
            return False
    return True

#2 functiom
def process_coin():
    print(" please insert coin")
    total = int(input("How many quarters :")) * 0.25
    total += int(input("How many dimes :")) * 0.1
    total += int(input("How many nickles :")) * 0.01
    total += int(input("How many pennies :")) * 0.05
    return total

#3 functiom
def is_transaction_sucessful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost)
        print(f"Here is ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Money has been refunded")
        return False

#4 functiom
def make_coffee(drink_name , order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


is_on = True
while is_on:
    choice = input(" What would you like ?(esp/latte/cap)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml ")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit} ")

    else:
        drink = MENU[choice]

        if complete_hai(drink['ingredients']):
            payment = process_coin()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(choice , drink["ingredients"])
