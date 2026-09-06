#%%
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

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}
profit = 0
is_on = True

def is_resource_suffiecient(order_ingredients):
    # Returns True when order can be amde, else False
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there isn't enough {item}")
            return False
    return True

def process_coins():
    # Retunrs total from coins inserted
    print("Please insert coins")
    total = int(input("how many quarters ")) * 0.25
    total += int(input("how many dimes ")) * 0.1
    total += int(input("how many nickles ")) * 0.05
    total += int(input("how many pennies ")) * 0.05
    return total

def is_transaction_sucessful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_recieved - drink_cost,2)
        return True
    else:
        print("Sorry that's not enough money.Money Refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    # Deduicting the required ingredients.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your{drink_name}")

while is_on:
    choice = input("What would you like? (expresso/latte/cappucino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money: $${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_suffiecient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_sucessful(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])

# %%
