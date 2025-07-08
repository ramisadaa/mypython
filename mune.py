import keyboard
import os

selected_index = 0

def on_key_event(e):
    global selected_index
    if e.name == 'up':
        selected_index = (selected_index - 1) % len(menu)
        
    elif e.name == 'down':
        selected_index = (selected_index + 1) % len(menu)
    elif e.name == 'esc':
        print("Exited.")
        keyboard.unhook_all()
        exit()
    elif e.name == 'enter':
        print(f"You selected: {menu[selected_index]}")
        # Here you can add functionality for the selected item

while True: 
    menu = ["Item 1", "Item 2", "Item 3", "Item 4"]
    for elem in menu :
        print (elem)
    keyboard.on_press(on_key_event)
    keyboard.wait('esc')
