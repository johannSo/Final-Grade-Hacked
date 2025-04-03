# Vor dem abgeben die "Debug:" sachen entfernen
# Import's:
from colorama import Fore, Style
import sys
import time
import secrets
import os

# Clear funktion:
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')

# Generate Password
passwd = secrets.token_urlsafe(5)

def slowprint(s): # Slowprint by https://gist.github.com/gnuton/3c7a46447d2be0aee0b2
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
    # Usage:
    # slowprint("Hello, test?")

# Funktionen
def anleitung():
    print("Debug: Julius, schreib hier mal die Anleitung rein!!!")
    while True:
        start = input("Willst du starten? (j/n): ").lower()
        if start == "j":
            print("Debug: Start")
            first()
            break
        elif start == "n":
            print("Bye 👋")
            exit()
        else:
            print("Bitte nur 'j' oder 'n' eingeben!")

def first():
    def first_abfrage():
        while True:
            clear()
            print("Du bist in das Zimmer des Schulleiters eingebrochen und hast den Laptop gefunden. Was willst du nun tun?")
            print(Fore.BLUE + "a) Den Laptop starten?" + Style.RESET_ALL)
            print(Fore.BLUE + "b) Die Festplatte kopieren?" + Style.RESET_ALL)
            print(Fore.BLUE + "c) Die Festplatte stehlen?" + Style.RESET_ALL)
            first = input("Was wählst du?: ").lower()
            if first == "a":
                print("Debug: Input: a")
                print("Der Laptop startet und du siehst ein Passwortfeld. Das Passwort weißt du nicht.")
                continue
            elif first == "b":
                print("Debug: Input: b")

            elif first == "c":
                print("Debug: Input: c")
                break
            else:
                print("Bitte nur 'a', 'b' oder 'c' eingeben!")
    first_abfrage()

anleitung()
