# Welcome to my vending machine assessment!

# Dictionary was used to organize the drinks, chips, snacks, and pastry.
item_menu = {
    #Drink items
    '𝙳𝚁𝙸𝙽𝙺𝚂': {
        "A1": {"item": "    𝙱𝚄𝙺𝙾 𝙹𝚄𝙸𝙲𝙴                        ", "price": 1.25, "category": "𝙳𝚁𝙸𝙽𝙺𝚂", "stock": 5},
        "A2": {"item": "    𝙼𝙾𝙶𝚄 𝙼𝙾𝙶𝚄                         ", "price": 1.00, "category": "𝙳𝚁𝙸𝙽𝙺𝚂", "stock": 5},
        "A3": {"item": "    𝚆𝙰𝚃𝙴𝚁                             ", "price": 1.15, "category": "𝙳𝚁𝙸𝙽𝙺𝚂", "stock": 5},
        "A4": {"item": "    𝚈𝙰𝙺𝚄𝙻𝚃                            ", "price": 1.50, "category": "𝙳𝚁𝙸𝙽𝙺𝚂", "stock": 5},
    },
    # Snack Items
    '𝚂𝙽𝙰𝙲𝙺𝚂': {
        "B1": {"item": "    𝙿𝙾𝙻𝚅𝙾𝚁𝙾𝙽                          ", "price": 2.25, "category": "𝚂𝙽𝙰𝙲𝙺𝚂", "stock": 5},
        "B2": {"item": "    𝙿𝙰𝚂𝚃𝙸𝙻𝙻𝙰𝚂                         ", "price": 2.75, "category": "𝚂𝙽𝙰𝙲𝙺𝚂", "stock": 5},
        "B3": {"item": "    𝙿𝚄𝚃𝙾                              ", "price": 2.15, "category": "𝚂𝙽𝙰𝙲𝙺𝚂", "stock": 5},
        "B4": {"item": "    𝚈𝙴𝙼𝙰                              ", "price": 2.25, "category": "𝚂𝙽𝙰𝙲𝙺𝚂", "stock": 5},
    },
    # Pastry Items
    '𝙿𝙰𝚂𝚃𝚁𝚈': {
        "C1": {"item": "    𝙴𝙽𝚂𝙰𝚈𝙼𝙰𝙳𝙰                         ", "price": 3.50, "category": "𝙿𝙰𝚂𝚃𝚁𝚈", "stock": 5},
        "C2": {"item": "    𝙷𝙾𝙿𝙸𝙰                             ", "price": 3.25, "category": "𝙿𝙰𝚂𝚃𝚁𝚈", "stock": 5},
        "C3": {"item": "    𝙱𝙸𝙺𝙾                              ", "price": 3.15, "category": "𝙿𝙰𝚂𝚃𝚁𝚈", "stock": 5},
        "C4": {"item": "    𝙿𝙰𝙽 𝙳𝙴 𝙲𝙾𝙲𝙾                       ", "price": 3.00, "category": "𝙿𝙰𝚂𝚃𝚁𝚈", "stock": 5},
    },
    '𝙲𝙷𝙸𝙿𝚂': {
        # Chips Items
        "D1": {"item": "    𝚃𝙾𝙼𝙸 𝙲𝙾𝚁𝙽 𝙵𝙻𝙰𝚅𝙾𝚁𝙴𝙳                ", "price": 5.50, "category": "𝙲𝙷𝙸𝙿𝚂", "stock": 5},
        "D2": {"item": "    𝙿𝙸𝙰𝚃𝙾𝚂 𝙲𝙷𝙴𝙴𝚂𝙴 𝙵𝙻𝙰𝚅𝙾𝚁𝙴𝙳            ", "price": 5.25, "category": "𝙲𝙷𝙸𝙿𝚂", "stock": 5},
        "D3": {"item": "    𝙾𝙸𝚂𝙷𝙸 𝙿𝚁𝙰𝚆𝙽 𝙲𝚁𝙰𝙲𝙺𝙴𝚁𝚂              ", "price": 5.15, "category": "𝙲𝙷𝙸𝙿𝚂", "stock": 5},
        "D4": {"item": "    𝙲𝙷𝙸𝙿𝙿𝚈 𝙱𝙰𝚁𝙱𝙴𝙲𝚄𝙴 𝙲𝙾𝚁𝙽 𝙵𝙻𝙰𝚅𝙾𝚁𝙴𝙳     ", "price": 5.00, "category": "𝙲𝙷𝙸𝙿𝚂", "stock": 5},
    },
}

# Suggestions for add-ons depends on the category.
recommendations = {
    "𝙳𝚁𝙸𝙽𝙺𝚂": "𝚆𝙰𝙽𝚃 𝚂𝙾𝙼𝙴 𝙿𝙰𝚂𝚃𝚁𝚈 𝙵𝙾𝚁 𝚈𝙾𝚄𝚁 𝙳𝚁𝙸𝙽𝙺?",
    "𝚂𝙽𝙰𝙲𝙺𝚂": "𝙳𝙾 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙲𝙷𝙸𝙿𝚂 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝚂𝙽𝙰𝙲𝙺𝚂?",
    "𝙲𝙷𝙸𝙿𝚂": "𝚆𝙾𝚄𝙻𝙳 𝚈𝙾𝚄 𝙻𝙸𝙺𝙴 𝚃𝙾 𝙰𝙳𝙳 𝚂𝙾𝙼𝙴 𝙳𝚁𝙸𝙽𝙺𝚂 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙲𝙷𝙸𝙿𝚂?",
    "𝙿𝙰𝚂𝚃𝚁𝚈": "𝙿𝙴𝚁𝙵𝙴𝙲𝚃 𝚃𝙸𝙼𝙴 𝚃𝙾 𝙰𝙳𝙳 𝚂𝙾𝙼𝙴 𝙳𝚁𝙸𝙽𝙺𝚂!"
}

# Displays the title of this assessment.
print(""" 
 ▄█                                                                                                                                                                      ▄█     
 ██    ▀████▀   ▀███▀███▀▀▀███▀███▄   ▀███▀███▀▀▀██▄ ▀████▀███▄   ▀███▀ ▄▄█▀▀▀█▄█    ▀████▄     ▄███▀     ██       ▄▄█▀▀▀█▄█████▀  ▀████▀▀████▀███▄   ▀███▀███▀▀▀███     ██     
 ▀▀      ▀██     ▄█   ██    ▀█  ███▄    █   ██    ▀██▄ ██   ███▄    █ ▄██▀     ▀█      ████    ████      ▄██▄    ▄██▀     ▀█ ██      ██    ██   ███▄    █   ██    ▀█     ▀▀     
          ██▄   ▄█    ██   █    █ ███   █   ██     ▀██ ██   █ ███   █ ██▀       ▀      █ ██   ▄█ ██     ▄█▀██▄   ██▀       ▀ ██      ██    ██   █ ███   █   ██   █              
           ██▄  █▀    ██████    █  ▀██▄ █   ██      ██ ██   █  ▀██▄ █ ██               █  ██  █▀ ██    ▄█  ▀██   ██          ██████████    ██   █  ▀██▄ █   ██████              
           ▀██ █▀     ██   █  ▄ █   ▀██▄█   ██     ▄██ ██   █   ▀██▄█ ██▄    ▀████     █  ██▄█▀  ██    ████████  ██▄         ██      ██    ██   █   ▀██▄█   ██   █  ▄           
            ▄██▄      ██     ▄█ █     ███   ██    ▄██▀ ██   █     ███ ▀██▄     ██      █  ▀██▀   ██   █▀      ██ ▀██▄     ▄▀ ██      ██    ██   █     ███   ██     ▄█           
             ██     ▄█████████████▄    ██ ▄████████▀ ▄████▄███▄    ██   ▀▀███████    ▄███▄ ▀▀  ▄████▄███▄   ▄████▄ ▀▀█████▀▄████▄  ▄████▄▄████▄███▄    ██ ▄██████████           
""")

# Displays a welcoming for the user.
print("\n═════════════════════════════════════════════════════☞ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝙼𝚈 𝚅𝙴𝙽𝙳𝙸𝙽𝙶 𝙼𝙰𝙲𝙷𝙸𝙽𝙴. 𝙿𝙻𝙴𝙰𝚂𝙴 𝚃𝙰𝙺𝙴 𝙰 𝙻𝙾𝙾𝙺 𝙰𝚃 𝙼𝚈 𝙼𝙴𝙽𝚄! ☜═══════════════════════════════════════════════════════\n")

def display_item_menu():
    print("\n═══════════════════════════════════════════════════════════════════════════════════ 𝙼𝙴𝙽𝚄 ════════════════════════════════════════════════════════════════════════════════════\n")
    for category, items in item_menu.items():
        print(f"                                              ═══════════════════════════════════════════════════════════════════════════════════")
        print(f"                                                     𝙲𝙾𝙳𝙴 𝙸𝙳                           {category}           𝙿𝚁𝙸𝙲𝙴    𝚂𝚃𝙾𝙲𝙺")
        print(f"                                              ═══════════════════════════════════════════════════════════════════════════════════")
        for code, details in items.items():
            print(f"                                                    𝙲𝙾𝙳𝙴 | {code}: {details['item']} | ${details['price']:.2f} | Stock: {details['stock']}")

# Asks the user to select an item
def get_user_choice():
    while True:
        code = input("\n                                                                ▶ 𝙿𝙻𝙴𝙰𝚂𝙴 𝙴𝙽𝚃𝙴𝚁 𝚃𝙷𝙴 𝙲𝙾𝙳𝙴 𝙸𝙳 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃: ").upper()
        for category_items in item_menu.values():
            if code in category_items:
                if category_items[code]["stock"] > 0:
                    return code
                else:
                    print("\n                                                     ❕𝙴𝚁𝚁𝙾𝚁: 𝚃𝙷𝙸𝚂 𝙸𝚃𝙴𝙼 𝙸𝚂 𝙾𝚄𝚃 𝙾𝙵 𝚂𝚃𝙾𝙲𝙺. 𝙿𝙻𝙴𝙰𝚂𝙴 𝚃𝚁𝚈 𝙰𝙽𝙾𝚃𝙷𝙴𝚁 𝙸𝚃𝙴𝙼.❕")
        print("\n                                                               ❕𝙴𝚁𝚁𝙾𝚁: 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙲𝙾𝙳𝙴 𝙸𝙳. 𝙿𝙻𝙴𝙰𝚂𝙴 𝚃𝚁𝚈 𝙰𝙶𝙰𝙸𝙽.❕")

# Handles and checks the money of the user inputted.
def get_user_money():
    while True:
        try:
            money = float(input("\n                                                                ▶ 𝙺𝙸𝙽𝙳𝙻𝚈 𝙸𝙽𝚂𝙴𝚁𝚃 𝚃𝙷𝙴 𝙰𝙼𝙾𝚄𝙽𝚃 𝚈𝙾𝚄'𝚁𝙴 𝙰𝙳𝙳𝙸𝙽𝙶: $"))
            if money > 0:
                return money
            else:
                print("\n                                                             ❕𝙴𝚁𝚁𝙾𝚁: 𝙿𝙻𝙴𝙰𝚂𝙴 𝙴𝙽𝚃𝙴𝚁 𝙰 𝙿𝙾𝚂𝙸𝚃𝙸𝚅𝙴 𝙰𝙼𝙾𝚄𝙽𝚃 𝙾𝙵 𝙼𝙾𝙽𝙴𝚈.❕")
        except ValueError:
            print("\n                                                    ❕𝙴𝚁𝚁𝙾𝚁: 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙸𝙽𝙿𝚄𝚃. 𝙿𝙻𝙴𝙰𝚂𝙴 𝙴𝙽𝚃𝙴𝚁 𝙰 𝚅𝙰𝙻𝙸𝙳 𝙰𝙼𝙾𝚄𝙽𝚃 𝙾𝙵 𝙼𝙾𝙽𝙴𝚈.❕")

# Suggesting addtional items from the users current item.
def suggest_item(category):
    if category in recommendations:
        print(f"\n                                                               ꧁ SUGGESTION: {recommendations[category]} ꧂")

# Dispense the chosen item depending on the code and money that was inputted.
def dispense_item(code, money):
    for category, items in item_menu.items():
        # Checks if the code is valid.
        if code in items:
            item = items[code]["item"] 
            price = items[code]["price"]
            if money >= price: # Checks if the user put enough money.
                change = money - price # Calculating the money.
                items[code]["stock"] -= 1 # Subtracting the item from the stock.
                print(f"\n                                                                       ↺ 𝙳𝙸𝚂𝙿𝙴𝙽𝙳𝙸𝙽𝙶... {item}")
                print(f"                                                                         REMAINING BALANCE: ${change:.2f}")
                suggest_item(items[code]["category"]) # Recommending add-on items.
                return
            # Error and asking to add more by trying again.
            else:
                print("\n                                                           ❕𝙴𝚁𝚁𝙾𝚁: 𝚈𝙾𝚄𝚁 𝙵𝚄𝙽𝙳𝚂 𝙰𝚁𝙴 𝙽𝙾𝚃 𝙴𝙽𝙾𝚄𝙶𝙷. 𝙿𝙻𝙴𝙰𝚂𝙴 𝙰𝙳𝙳 𝙼𝙾𝚁𝙴❕")
                additional_money = get_user_money() # Additional fund.
                dispense_item(code, money + additional_money) # Trying to dispense again with the updated amount.
                return

def main():
    while True:
        display_item_menu() # Displays the menu.
        code = get_user_choice() # Takes the users chosen item code.
        money = get_user_money() # Takes the amount of money that the user inputed.
        dispense_item(code, money) # Dispensing the selected item.
        # Asking the user for more items.
        more_items = input("\n                                                             ▶ 𝙳𝙾 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙿𝚄𝚁𝙲𝙷𝙰𝚂𝙴 𝙰𝙽𝙾𝚃𝙷𝙴𝚁 𝙸𝚃𝙴𝙼? (𝚈𝙴𝚂 / 𝙽𝙾): ").lower()
        if more_items != 'yes': # The loop when exist if the use dont want any more items.
            break
        # Program ended.
    print("\n                                                            𝚃𝙷𝙰𝙽𝙺 𝚈𝙾𝚄 𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝙼𝚈 𝚅𝙴𝙽𝙳𝙸𝙽𝙶 𝙼𝙰𝙲𝙷𝙸𝙽𝙴! 𝙷𝙰𝚅𝙴 𝙰 𝙶𝚁𝙴𝙰𝚃 𝙳𝙰𝚈!")

# This only runs when the script is run directly.
if __name__ == "__main__":
    main()