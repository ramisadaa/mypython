import keyboard
import os

# ANSI escape codes for reverse video (swap foreground/background)
REVERSE = '\033[7m'
RESET = '\033[0m'

print("Use the arrow keys to control. Press ESC to exit.")
# Virtual menu
menu = ["Item 1", "Item 2", "Item 3", "Item 4"]
selected_index = 0

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, item in enumerate(menu):
        if i == selected_index:
            # Reverse video for highlight (black text on white background)
            print(f"{REVERSE}{item}{RESET}")
        else:
            print(f"  {item}")
    print("\nUse the arrow keys to navigate and ESC to exit.\n")

def on_key_event(e):
    global selected_index
    if e.name == 'up':
        selected_index = (selected_index - 1) % len(menu)
        print_menu()
    elif e.name == 'down':
        selected_index = (selected_index + 1) % len(menu)
        print_menu()
    elif e.name == 'esc':
        print("Exited.")
        keyboard.unhook_all()
        exit()
    elif e.name == 'enter':
        print(f"You selected: {menu[selected_index]}")
        # Here you can add functionality for the selected item
        

print_menu()
keyboard.on_press(on_key_event)
keyboard.wait('esc')
