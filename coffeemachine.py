MENU={
    "espresso": {
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappaccino":{
        "ingredients":{
            "water": 250,
            "milk" : 100,
            "coffee" :24,
        },
        "cost": 3.0,
    }

}

profit=0

resources= {
    "water": 300,
    "milk" :200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required  ingredients from the resources."""
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"Here is your {drink_name} 🍵")
    
            
def process_coins():
    """returns total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters?: "))* 0.25
    total += int(input("How many dimes?: "))* 0.1
    total += int(input("How many nickles?: "))* 0.05
    total += int(input("How many pennies?: "))* 0.01
    return total
    
def is_transaction_successful(money_received, drink_cost):
    """Return true if payment is accepted, False if payment is insufficient"""
    if money_received >= drink_cost:
        change= round(money_received- drink_cost, 2)
        print(f"Here is ${change} in  change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

is_on=True

while is_on:
    choice=input("What would you like? (espresso/latte/cappaccino): ")
    if choice == "off":
        is_on=False
    elif choice=="bill":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")      
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
            
            