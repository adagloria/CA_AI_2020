from commands import commands
import constants


def run():
    print("PYTHON_VERSION:", constants.PYTHON_VERSION)
    while True:
        command = input("Choose a command to run:\n")
        if not command:
            break
        if command not in commands:
            print("I do not recognize this command.")
            continue
        commands[command]()

    print("Goodbye!")


if __name__ == "__main__":
    run()
