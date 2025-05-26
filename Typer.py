import pyautogui
import time
import keyboard

# Java code to be typed
code = """


[PUT TO TYPE SCRIPT HERE]


"""

# Auto-completed opening/closing characters — exclude quotes here
auto_open = {'(': ')', '{': '}'}
auto_close = set(auto_open.values())

# Countdown before typing starts
print("")
time.sleep(3)
print("[*] Input saved!")
time.sleep(0.5)
print("[!] Getting ready to type...")
time.sleep(1)
print("[*] Typing in: 3")
time.sleep(1)
print("[*] Typing in: 2")
time.sleep(1)
print("[*] Typing in: 1")
time.sleep(0.4)
print("[!] Typing!")

time.sleep(1)

i = 0
while i < len(code):
    if keyboard.is_pressed('backspace'):
        print("\n[!] Typing cancelled by user.")
        break

    char = code[i]
    next_char = code[i+1] if i+1 < len(code) else ''

    if char == '\n':
        pyautogui.press('enter')
    elif char == '\t':
        pyautogui.press('tab')

    # Handle opening brackets that auto-complete
    elif char in auto_open and next_char == auto_open[char]:
        pyautogui.typewrite(char)  # type opening char
        time.sleep(0.02)           # slight delay for autocomplete
        pyautogui.press('right')   # skip the auto-inserted closing char
        i += 1                    # skip next char in code

    # For closing brackets only — skip by pressing right
    elif char in auto_close:
        pyautogui.press('right')

    else:
        # Always type quotes explicitly, never skip them
        pyautogui.typewrite(char)

    i += 1
    time.sleep(0.01)
