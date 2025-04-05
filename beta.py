# Vor dem abgeben die "Debug:" sachen entfernen
# Import's:
from colorama import Fore, Style
import sys
import time
import secrets
import os

# Variables:
slp = time.sleep

# Clear funktion:
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
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
            a()
            break
        elif start == "n":
            print("Bye 👋")
            exit()
        else:
            print("Bitte nur 'j' oder 'n' eingeben!")

def a():
    def first_abfrage():
        while True:
            print("\n")
            print("Debug: Ich hab keine ahnung was hier rein soll, JULIUS mach was! (;")
            print(Fore.BLUE + "a) Lernen für die nächsten Tests 📚" + Style.RESET_ALL)
            print(Fore.BLUE + "b) In das Büro des Schulleiters einbrechen 🔑" + Style.RESET_ALL)
            print(Fore.BLUE + "c) Einen Hack auf die beste.schule server starten 🖥️" + Style.RESET_ALL)
            first = input("Was wählst du?: ").lower()
            if first == "a":
                print(Fore.MAGENTA + "Du hast kein Bock zu lernen und giebst nach 30min auf." + Style.RESET_ALL)
                continue
            elif first == "b":
                b()
                break
            elif first == "c":
                c = input("Bist du dir sicher das du Starten willst")
                if c == "j":
                    print("Du bereitest alles vor und startest dein Hacking program 💻")
                    slp(1)
                    print("Output:")
                    slowprint(Fore.GREEN + "Hack failed, security to high" + Style.RESET_ALL)
                    slp(2)
                    print(Fore.RED + "Am abend bekommst du eine E-Mail in der steht das man den Hack auf dich zurrück verfolgen konnte und du einen Schulverweß bekommst 😭")
                    slp(10)
                    clear()
                    print("Deine eltern regen sich auf warum du sowas machst und sie nehmen dir deinen PC weg und zwingen dich zum Lernen")
                    print("Du bleibts trozdem sitzen!\nGame Over 😭")
                    exit()
                elif c == "n":
                    continue
                else:
                    print(Fore.LIGHTRED_EX + "Bitte nur 'a', 'b' oder 'c' eingeben!" + Style.RESET_ALL)
            else:
                print("Bitte nur 'a', 'b' oder 'c' eingeben!")
    first_abfrage()

def b():
    print(Fore.RED + "Du steckst dein USB stick ein und erstellst ein eins zu ein kopie der Festplatte." + Style.RESET_ALL)
    print(Fore.GREEN + "Du verlässt das Büro des Schulleiters wieder." + Style.RESET_ALL)
    print(Fore.GREEN + "Du startest über deinen Privaten PC eine offline Bruteforce attacke" + Style.RESET_ALL)
    print("Output deines Terminals:")
    slowprint(Fore.LIGHTGREEN_EX + "No password match found, should I try again with a bigger database? (y/n):" + Style.RESET_ALL)
    b = input("").lower()
    if b == "y":
        slowprint("Retrying with 40GB database!")
        slp(2)
        slowprint("Success: password is: " + "'" + passwd + "'")
        slp(3)
        final()
    elif b == "n":
        print("Debug: n")
    else:
        print("Bitte nur 'a', 'b' oder 'c' eingeben!")

def final():
    print("Du hast das Passwort heraus gefunden ")

anleitung()
