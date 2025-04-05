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
    print("Willkomen. Um Optionen auszuwählen gieb den buchstaben davor ein und drücke enter. Du hast das Game geschaft wenn du deine Endjahresnote durch hacken verbessert hast und das Jahr bestehst")
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
            print("Du musst es schaffen zu bestehen, was machst du?")
            print(Fore.BLUE + "a) Lernen für die nächsten Tests 📚" + Style.RESET_ALL)
            print(Fore.BLUE + "b) In das Büro des Schulleiters einbrechen 🔑" + Style.RESET_ALL)
            print(Fore.BLUE + "c) Einen Hack auf die Schulserver starten 🖥️" + Style.RESET_ALL)
            print(Fore.BLUE + "d) Die Lehrer bestechen 💵" + Style.RESET_ALL)
            print(Fore.BLUE + "Drücke h für das hilfe menu 🧑‍⚕️" + Style.RESET_ALL)
            first = input("Was wählst du?: ").lower()
            if first == "a":
                print(Fore.RED + "Du hast kein Bock zu lernen und giebst nach 30 minuten auf." + Style.RESET_ALL)
                continue
            elif first == "b":
                b()
            elif first == "c":
                c = input("Bist du dir sicher das du Starten willst").lower()
                if c == "j":
                    print("Du bereitest alles vor und startest dein Hacking program 💻")
                    slp(1)
                    print("Output:")
                    slowprint(Fore.GREEN + "Hack failed, security to high" + Style.RESET_ALL)
                    slp(2)
                    print(Fore.RED + "Am abend bekommst du eine E-Mail in der steht das man den Hack auf dich zurrück verfolgen konnte und du einen Schulverweiß bekommst 😭")
                    slp(10)
                    clear()
                    print("Deine eltern regen sich auf warum du sowas machst und sie nehmen dir deinen PC weg und zwingen dich zum Lernen")
                    print("Du bleibts trozdem sitzen!\nGame Over 😭")
                    exit()
                elif c == "n":
                    clear()
                    print("Game Over 😭")
                    exit()
            elif first == "d":
                print("Die Lehrer lassen sich leider nicht bestechen 💵")
                slp(1)
                print("Game Over 😭")
                exit()
            elif first == "h":
                help()
            else:
                print("Bitte nur 'a', 'b', 'c' oder 'd' eingeben!")
    first_abfrage()

def b(): # Ganz b noch neu
    print("Du gehst zu Büro deines Schulleiters und knackst das Schloss!")
    print("In seinem Büro findest du:")
    print("     Seinen Laptop der aber Verschlüsselt ist 🔒")
    print("     Einen Schlüssel 🔑")
    print("     Einen Tresor 🏦")
    slp(15)
    clear()
    print("a) Den Schlüssel am Tresor probieren?\nb) Den Laptop kopieren?\nc) Den Laptop klauen?")
    b = input(Fore.CYAN + "Was willst du tun?" + Style.RESET_ALL)
    if b == "a":
        clear()
        print("Er passt aber darin sind nur Dokumente und Bargeld")

def final():
    print("Du hast das Passwort heraus gefunden!")
    print("Du logs dich ein und änderst deine Noten so das du bestehst aber es nicht auffällt.")
    print("Du bestehst das Schuljahr und dein Eltern freuen sich.")
    print("Sie fragen sich aber auch wie du das geschaft hast. Du erzälst eine Lüge und sie glauben dir.")
    print("Du bekommst einen neuen Laptop und gehst zufrieden in die Sommerferien.")

def help():
    print("a) Was ist bruteforce\nb) Creditst")
    help = input("Was willst du?")
    if help == "a":
        clear()
        print("Brute-Force bezeichnet eine Angriffsmethode in der IT-Sicherheit, bei der alle möglichen Kombinationen von Passwörtern oder Schlüsseln systematisch ausprobiert werden, um Zugang zu einem geschützten System zu erhalten. Diese Methode ist sehr rechenintensiv und zeitaufwendig, wird jedoch häufig dann eingesetzt, wenn keine Schwachstellen im System vorliegen.")
        exit()
    elif help == "b":
        credits()
    else:
        print("Bitte nur 'a' oder 'b' eingeben!")

def credits():
    clear()
    print("Game: Final Grade Hacked\nGit: https://github.com/johannSo/Final-Grade-Hacked\nAuthors: Jonathan Soppa, Julius Brückner\nTools: Zed, GitHub")

anleitung()
