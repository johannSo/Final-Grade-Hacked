# Import's:
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
def los():
    print("Julius, schreib hier mal die Anleitung rein!!!")
    erstens()

def erstens():
    slowprint("Hallo")

## Start
while True:
    start = input("Willst du starten? (j/n): ").lower()
    if start == "j":
        print("Lets go")
        los()
        break
    elif start == "n":
        print("Bye 👋")
        exit()
    else:
        print("Bitte nur 'j' oder 'n' eingeben!")
