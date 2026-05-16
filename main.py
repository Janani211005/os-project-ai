import os
import requests

def ask_ai(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        return res.json()["response"]
    except:
        return "AI not running!"

while True:
    cmd = input(">>> ").lower()

    # exit
    if "exit" in cmd:
        print("Bye 👋")
        break

    # 🧠 universal open (ANY app)
    elif cmd.startswith("open "):
        app = cmd.replace("open ", "")
        os.system(f"start {app}")

    # 🧮 calculator
    elif "calc" in cmd:
        try:
            expr = cmd.replace("calc", "")
            print("Result:", eval(expr))
        except:
            print("Invalid calculation")

    # default → AI
    else:
        print("AI:", ask_ai(cmd))