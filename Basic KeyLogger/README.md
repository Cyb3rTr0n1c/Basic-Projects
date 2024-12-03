### 🔑 Keylogger Project Repository

This repository hosts a Python-based keylogger that demonstrates how to capture and log keyboard inputs effectively. The project is built for educational purposes, emphasizing key event handling, modifier key states, and combination detection using the `pynput` library.

---

## 📋 Keylogger Project Overview

### 🎯 Objective
To create a keylogger that logs keyboard activity, including individual key presses and key combinations like `Ctrl+C`. The logger writes the output to a file in a readable format.

---

### 🛠️ Features
- Logs both regular and special keys.
- Detects and logs key combinations with modifiers (`Ctrl`, `Shift`, `Alt`).
- Handles ASCII control characters (e.g., `Ctrl+C`) with human-readable mapping.

---

### 📝 Implementation Steps
1. **Environment Setup**:
   - Install the required library using:  
     ```bash
     pip install pynput
     ```
2. **Logic for Key Events**:
   - Detect and log individual key presses.
   - Handle modifier keys and their combinations dynamically.
3. **Readable Output**:
   - Map control characters to readable equivalents (e.g., `Ctrl+C`).
   - Format output for clarity in both console and log file.

---

### 🚀 Output Example
- Pressing `Ctrl+C` logs: `[Ctrl+C]`
- Pressing `Enter` logs: `[Enter]`
- Pressing `Shift+A` logs: `[Shift+A]`

---

### ⚠️ Disclaimer
This project is for educational purposes only. Unauthorized use of keylogging software may violate privacy laws or regulations. Always ensure compliance with applicable laws before using or sharing.

---

### 📚 References
- [pynput Documentation](https://pynput.readthedocs.io/en/latest/)  
- [ASCII Control Characters](https://en.wikipedia.org/wiki/Control_character)  
