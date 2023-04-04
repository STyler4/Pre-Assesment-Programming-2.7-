import easygui

combos = {}

while True:
    choice = easygui.buttonbox("What would you like to do?", "Burger Combos", ["Add Combo", "Find Combo", "Delete Combo", "Output All", "Exit"])

    if choice == "Add Combo":
        name = easygui.enterbox("Enter the combo name:").upper()

        combos[name] = None

    elif choice == "Find Combo":
        name = easygui.enterbox("Enter the combo name to search for:").upper()

        if name in combos:
            if combos[name] is not None:
                easygui.msgbox(f"{name}: ${combos[name]:.2f}")
            else:
                easygui.msgbox(f"{name}: price not set")
        else:
            easygui.msgbox(f"{name} not found.")

    elif choice == "Delete Combo":
        name = easygui.enterbox("Enter the combo name to delete:").upper()

        if name in combos:
            del combos[name]
            easygui.msgbox(f"{name} deleted.")
        else:
            easygui.msgbox(f"{name} not found.")

    elif choice == "Output All":
        output = ""
        for name, price in combos.items():
            if price is not None:
                output += f"{name}: ${price:.2f}\n"
            else:
                output += f"{name}: price not set\n"
        easygui.msgbox(output)

    elif choice == "Exit":
        break
