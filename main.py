from face_auth import authenticate
from voice_command import get_voice_command, get_text_command
from command_executor import execute

def main():
    print("🔐 Face Authentication Required")

    if authenticate():
        print("🎤 Give Command (voice/text)")

        choice = input("1. Voice  2. Text: ")

        if choice == "1":
            command = get_voice_command()
        else:
            command = get_text_command()

        print("👉 Command received:", command)   # DEBUG

        if command:
            execute(command)
        else:
            print("❌ No command detected")

    else:
        print("❌ Authentication Failed")

if __name__ == "__main__":
    main()
