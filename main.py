import os
while True:
    cmd = input(">>> ")
    if "open chrome" in cmd:
        os.system("start chrome")
    elif "open notepad" in cmd:
        os.system("notepad")
    elif "exit" in cmd:
        break
    else:
        print("Command not found")