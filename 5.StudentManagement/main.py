import sys
from auth.login import show_login_window
from auth.registration import show_registration_window

def main():
    """Run administrative tasks."""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "login":
            show_login_window()
        elif command == "register":
            show_registration_window()
        else:
            print("Unknown command")
    else:
        print("Usage: python main.py [login|register]")

if __name__ == '__main__':
    main()


##! To run:-
## python main.py login
## python main.py register
