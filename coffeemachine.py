MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": { "ingredients": {"water": 200,"milk": 150,"coffee": 24, }, "cost": 2.5,},
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
    "money" :0,
}
def check_resources(water,milk,coffee):
    on=True
    if resources["water"]<water:
        print("Sorry there is not enough water in the machine.")
        return on is False
    if resources["milk"]<milk:
        print("Sorry there is not enough milk in the machine.")
        return on is False
    if resources["coffee"] < coffee:
        print("Sorry there is not enough coffee in the machine.")
        return on is False



# on_off=input("Do you want to on the machine?:Yes or No : ").lower()
# if on_off=="yes":
on=True
while on is True:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=="report":
        print(f"Water :{resources['water']}ml\nMilk :{resources['milk']}ml\nCoffee :{resources['coffee']}g\nMoney :${resources['money']}")
    cont=check_resources(MENU[choice]["ingredients"]["water"], MENU[choice]["ingredients"]["milk"], MENU[choice]["ingredients"]["coffee"])
    if cont==False:
        break
    print("Please insert money.")
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))
    #quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    monetary_value = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    
    if monetary_value<MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    if monetary_value>=MENU[choice]["cost"]:
        resources["money"] += MENU[choice]["cost"]
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -=MENU[choice]["ingredients"]["coffee"]
        print(f"Here is your {choice}, Enjoy!")
        if monetary_value>MENU[choice]["cost"]:
           refund = round((monetary_value-MENU[choice]["cost"]),2)
           print(f"Here is your ${refund} dollars in change.")




























# else:
#     on=False

