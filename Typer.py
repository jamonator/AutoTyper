import pyautogui
import time
import keyboard

# Code to be typed
code = """


[PUT TO TYPE SCRIPT HERE]


"""

auto_open = {'(': ')', '{': '}'}
auto_close = set(auto_open.values())

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


    elif char in auto_open and next_char == auto_open[char]:
        pyautogui.typewrite(char) 
        time.sleep(0.02)         
        pyautogui.press('right')  
        i += 1                

    elif char in auto_close:
        pyautogui.press('right')

    else:
        pyautogui.typewrite(char)

    i += 1
    time.sleep(0.01)
