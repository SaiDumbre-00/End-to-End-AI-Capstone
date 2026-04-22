import os
import webbrowser
import datetime

def execute(command):
    command = command.lower()

    if "youtube" in command:
        print("▶️ Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        print("🌐 Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "notepad" in command:
        print("📝 Opening Notepad...")
        os.system("notepad")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("⏰ Current Time:", current_time)

    elif "exit" in command:
        print("👋 Exiting...")
        exit()

    else:
        print("❌ Command not recognized")
