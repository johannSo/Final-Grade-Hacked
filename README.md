# 💻 Final Grade: Hacked
## Story
Der Spieler ist ein Hacker und soll sich in den Laptop seines Schulleiters rein hacken um dort über `beste.schule` seine Noten von Versetzungsgefährdet auf 3 umzuändern, damit er zur Zeugnissausgabe einen neuen PC bekommt.

### Technische details
Er nutzt Ubuntu was mit LUKS verschlüsselt ist, deshalb erstellen wir eine Kopie der disk um dann eine Offline 'Brute force' Attacke zu starten, und die Datei `passwd.txt` zu klauen und dann unsere noten zu ändern.

## Installation
Install dependencies
```bash
pip3 install -r requirements.txt
```
And run the Code
```bash
python3 src/main.py
```

## Charaktere
- Hackerman
- Schulleiter

## Aktivitäten
- Hacken (Brute force attacke)

## Orte
- Schule
- Zuhause

## Gegenstände
- Laptop (vom Schulleiter)
- PC (vom Hackerman)
- SSD
- Disk Kopie