# Imports:
from colorama import Fore, Style
import sys
import time
import secrets
import os

# Variablen:
slp = time.sleep

# "clear" Funktion:
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Passwort generieren 🔑
passwd = secrets.token_urlsafe(5)

def slowprint(s):  # Slowprint by https://gist.github.com/gnuton/3c7a46447d2be0aee0b2
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 10)

# Funktionen 🎮
def anleitung():
    print("Willkommen! 🎉 Um Optionen auszuwählen, gib den Buchstaben davor ein und drücke Enter.")
    print("Du hast das Game geschafft, wenn du deine Endjahresnote verbessert hast und das Jahr bestehst! 📚")
    while True:
        start = input("Willst du starten? (j/n): ").lower()
        if start == "j":
            a()
            break
        elif start == "n":
            print("Bye 👋")
            exit()
        else:
            print("Bitte nur 'j' oder 'n' eingeben! ⚠️")

def a():
    def first_abfrage():
        while True:
            print("Du musst es schaffen zu bestehen, was machst du? 🤔")
            print(Fore.BLUE + "a) Lernen für die nächsten Tests 📚" + Style.RESET_ALL)
            print(Fore.BLUE + "b) In das Büro des Schulleiters einbrechen 🔑" + Style.RESET_ALL)
            print(Fore.BLUE + "c) Einen Hack auf die Schulserver starten 🖥️" + Style.RESET_ALL)
            print(Fore.BLUE + "d) Die Lehrer bestechen 💵" + Style.RESET_ALL)
            print(Fore.BLUE + "Drücke h für das Hilfe-Menü 🆘" + Style.RESET_ALL)
            first = input("Was wählst du?: ").lower()
            if first == "a":
                clear()
                print(Fore.RED + "Du hast keinen Bock zu lernen und gibst nach 30 Minuten auf. 😴" + Style.RESET_ALL)
                continue
            elif first == "b":
                b()
            elif first == "c":
                c = input("Bist du dir sicher, dass du starten willst? (j/n): ").lower()
                if c == "j":
                    print("Du bereitest alles vor und startest dein Hacking-Programm 💻")
                    slp(1)
                    print("Output:")
                    slowprint(Fore.GREEN + "Hack failed, Security zu hoch! 🚨" + Style.RESET_ALL)
                    slp(2)
                    print(Fore.RED + "Am Abend bekommst du eine E-Mail, in der steht, dass man den Hack auf dich zurückverfolgen konnte! 😨 Schulverweis!" + Style.RESET_ALL)
                    slp(10)
                    clear()
                    print("Deine Eltern rasten aus! 😡 Sie nehmen dir deinen PC weg und zwingen dich zum Lernen. 💀")
                    print("Du bleibst trotzdem sitzen!\nGame Over 😭")
                    exit()
                elif c == "n":
                    clear()
                    print("Game Over 😭")
                    exit()
                else:
                    print("Bitte nur 'j' oder 'n' eingeben! ⚠️")
            elif first == "d":
                print("Die Lehrer lassen sich leider nicht bestechen! 💵❌")
                slp(1)
                print("Game Over 😭")
                exit()
            elif first == "h":
                help()
            else:
                print("Bitte nur 'a', 'b', 'c' oder 'd' eingeben! ⚠️")
    first_abfrage()

def b():
    print(Fore.BLUE + "Du gehst ins Büro des Schulleiters und knackst das Schloss! 🔓" + Style.RESET_ALL)
    print("In seinem Büro findest du:")
    print("     🔒 Seinen Laptop (verschlüsselt)")
    print("     🔑 Einen Schlüssel")
    print("     🏦 Einen Tresor")
    slp(15)
    clear()
    while True:
        print("a) Den Schlüssel am Tresor probieren? 🏦")
        print("b) Den Laptop kopieren? 💾")
        print("c) Den Laptop klauen? 💻")
        b = input(Fore.CYAN + "Was willst du tun? " + Style.RESET_ALL)
        clear()
        if b == "a":
            print("Der Schlüssel passt, aber darin sind nur Dokumente und Bargeld. 💵❌")
            continue
        elif b == "b":
            print("Du steckst deine SSD ein und startest den Kopiervorgang. 💾")
            slp(2)
            print("Zu Hause angekommen, versuchst du den Laptop zu knacken. 🔓")
            slp(2)
            print("Output deines Hacking-Programms:")
            slowprint(Fore.GREEN + "Bruteforce 10% done" + Style.RESET_ALL)
            slp(1)
            slowprint(Fore.GREEN + "Bruteforce 30% done" + Style.RESET_ALL)
            slp(1)
            slowprint(Fore.GREEN + "Bruteforce 60% done" + Style.RESET_ALL)
            slp(1)
            slowprint(Fore.GREEN + "Bruteforce 90% done" + Style.RESET_ALL)
            slp(1)
            slowprint(Fore.GREEN + "Bruteforce 100% done" + Style.RESET_ALL)
            print("Du hast das Passwort gefunden! 🎉")
            slp(2)
            print("Das Passwort ist: " + Fore.GREEN + passwd + Style.RESET_ALL)
            slp(2)
            final()
        elif b == "c":
            print("Du nimmst den Laptop mit und versuchst ihn zu knacken... 🖥️💀")
            slp(2)
            print("Aber der Lehrer checkt die Überwachungsanlage! 📹🚨")
            slp(2)
            print("Die Polizei wird gerufen, du wirst verhaftet! 👮‍♂️❌")
            slp(2)
            print("Schulverweis und du bleibst sitzen. 😭")
            print("Game Over!")
            exit()

def final():
    final = input("beste.schule: Gib das Passwort ein: ")
    if final == passwd:
        print("Du hast das Passwort herausgefunden! 🎉")
        slp(2)
        print("Du loggst dich ein und änderst deine Noten unauffällig. 🖥️✅")
        slp(2)
        print("Deine Eltern freuen sich über deine 'Leistung' und schenken dir einen neuen Laptop! 😆💻")
        print("Game Completed! 🎊")
    else:
        print(Fore.RED + "Falsches Passwort! 😭" + Style.RESET_ALL)
        slp(1)
    exit()

def help():
    print("a) Was ist Bruteforce? 🔐\nb) Credits 📜")
    help = input("Was willst du? ")
    if help == "a":
        clear()
        print("Bruteforce ist eine Angriffsmethode, bei der alle möglichen Passwortkombinationen ausprobiert werden. 💻🚀")
        exit()
    elif help == "b":
        credits()
    else:
        print("Bitte nur 'a' oder 'b' eingeben! ⚠️")

def credits():
    clear()
    print("Game: Final Grade Hacked 🎮\nGitHub: https://github.com/johannSo/Final-Grade-Hacked\nAutoren: Jonathan Soppa, Julius Brückner")

anleitung()
