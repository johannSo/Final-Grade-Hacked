# Import's:
from colorama import Fore, Style
import sys
import time
import secrets

# Generate Password
passwd = secrets.token_urlsafe(5)

def slowprint(s): # Slowprint von https://gist.github.com/gnuton/3c7a46447d2be0aee0b2
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
    # Usage:
    # slowprint("Hello, test?")

# Funktionen
def anleitung():
    print("Julius, schreib hier mal die Anleitung rein!!!")
    while True:
        start = input("Willst du starten? (j/n): ").lower()
        if start == "j":
            print("Lets go")
            first()
            break
        elif start == "n":
            print("Bye 👋")
            exit()
        else:
            print("Bitte nur 'j' oder 'n' eingeben!")

def first():
    print("Du bist in das Zimmer des Schulleiters eingebrochen und hast den Laptop gefunden. Was willst du nun tun?")
    print(Fore.BLUE + "Den Laptop starten?" + Style.RESET_ALL)
    print(Fore.BLUE + "Die Festplatte kopieren?" + Style.RESET_ALL)
    print(Fore.BLUE + "Die Festplatte stehlen?" + Style.RESET_ALL)
    while True:
        first = input("Willst du starten? (j/n): ").lower()
        if first == "j":
            print("Lets go")
            break
        elif first == "n":
            print("Bye 👋")
            exit()
        else:
            print("Bitte nur 'j' oder 'n' eingeben!")

anleitung()
