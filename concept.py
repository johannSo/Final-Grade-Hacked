import time
import random

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def choose_option(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Wähle eine Option: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("Ungültige Eingabe, versuche es erneut.")

def hack_laptop():
    print_slow("Du bist ein Hacker und willst deine Noten auf 'beste.schule' ändern...")
    time.sleep(1)

    print_slow("1. Zugriff auf den Laptop des Schulleiters...")
    time.sleep(2)
    print_slow("Gefunden: Verschlüsselte LUKS-Festplatte!")
    time.sleep(1)

    print_slow("Was willst du tun?")
    choice = choose_option(["Live-System nutzen", "Festplatte direkt angreifen"])
    if choice == 1:
        print_slow("Du bootest mit einem USB-Live-System...")
    else:
        print_slow("Du versuchst, die Festplatte direkt zu entschlüsseln...")

    print_slow("2. Erstelle eine Kopie der Festplatte...")
    for i in range(1, 101, 20):
        print_slow(f"Kopieren... {i}% abgeschlossen")
        time.sleep(1)
    print_slow("Festplattenkopie erfolgreich erstellt!\n")

    print_slow("3. Starte Brute-Force-Attacke auf LUKS-Verschlüsselung...")
    attempts = 0
    success = False

    while not success:
        attempts += random.randint(5000, 10000)
        print_slow(f"Versuch #{attempts}: Keine Übereinstimmung...")
        time.sleep(0.5)
        if random.random() < 0.2:  # 20% Chance pro Durchlauf
            success = True

    print_slow(f"Treffer gefunden nach {attempts} Versuchen! Zugriff gewährt.\n")

    print_slow("4. Suche nach der Datei 'passwd.txt'...")
    time.sleep(2)
    print_slow("Datei gefunden! Extrahiere Passwort...\n")

    print_slow("Was willst du als nächstes tun?")
    choice = choose_option(["Passwort direkt nutzen", "Mehr Informationen sammeln"])
    if choice == 2:
        print_slow("Du findest zusätzlich Admin-Zugangsdaten!")

    print_slow("5. Einloggen bei 'beste.schule'...")
    time.sleep(2)
    print_slow("Passwort akzeptiert! Zugriff auf Noten erhalten.")

    print_slow("6. Ändere Noten von 'versetzungsgefährdet' auf '3'...")
    time.sleep(2)
    print_slow("Noten erfolgreich geändert!\n")

    print_slow("Was willst du tun?")
    choice = choose_option(["Spuren löschen", "System offen lassen"])
    if choice == 1:
        print_slow("Erfolgreich abgemeldet und Spuren gelöscht.")
    else:
        print_slow("System offen gelassen... Risiko erhöht! 😈")

    print_slow("Der Hack war ein voller Erfolg! 🎉")

if __name__ == "__main__":
    hack_laptop()
