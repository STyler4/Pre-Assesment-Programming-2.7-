"""Create A Welcome Screen using easygui"""

import easygui

name = easygui.enterbox("What is your name")
symbol = "!"
text = "WELCOME TO BURGER MENU COMBOS"
sides = symbol * 3

formatted_text = f"{sides} {text} {name.upper()} {sides}"
top_bottom = symbol * len(formatted_text)

easygui.msgbox(formatted_text)

