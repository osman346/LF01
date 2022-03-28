import string
import random
from colorama import Fore

#  Eingabe
passwort = input("Geben Sie bitte ein Passwort ein.\n")
status = 0

#  Besitzt das Passwort Sonderzeichen, Großbuchstaben, Kleinbuchstaben und Ziffern?
sonderzeichen = ['!', '§', '$', '%', '&', '/', '(', ')', '=', '?', 'ß', "'", '"', '*', '#', '.', '_', '-', ';', ',',
                 '~', '+', ']', '[', '}', '{', '<', '>', '|', '@', '^', '°', ':', '€', 'µ', '´', '`', ' ']

for a in sonderzeichen:
    if a in passwort:
        status += 1
        break

grossbuchstabe = string.ascii_uppercase  # Beinhaltet alle Großenbuchstaben.
for b in grossbuchstabe:
    if b in passwort:
        status += 1
        break

kleinbuchstabe = string.ascii_lowercase  # Beinhaltet alle Kleinenbuchstaben.
for c in kleinbuchstabe:
    if c in passwort:
        status += 1
        break

ziffer = string.digits  # Beinhaltet alle Zahlen.
for d in ziffer:
    if d in passwort:
        status += 1
        break

#  Passwort Länge
if len(passwort) >= 10:
    status += 1
else:
    print(Fore.RED + "Ihr Passwort beinhaltet keine 10 Zeichen.")
    status -= 1

#  Übeprüfung, welchen Wert der Status hat
if status == 5:
    print(Fore.CYAN + "Ihr Passwort ist stark.")
elif status == 3 or status == 4:
    print(Fore.GREEN + "Ihr Passwort ist gut.")
elif status == 2:
    print(Fore.YELLOW + "Ihr Passwort ist okay.")
elif status == 1:
    print(Fore.RED + "Ihr Passwort ist schwach.")
else:
    print(Fore.BLUE + "Ihr Passwort ist sehr schwach oder Sie besitzen keins.")

#  Rückgabe
if not a in passwort:
    print("Ihnen fehlen Sonderzeichen.")
if not b in passwort:
    print("Ihnen fehlen Grossbuchstaben.")
if not c in passwort:
    print("Ihnen fehlen Kleinbuchstaben.")
if not d in passwort:
    print("Ihnen fehlen Zahlen.")

# Neues Passwort
gen = input("Möchten Sie ein Passwort generieren? (J/N)\n")

if gen == "J":
    print("Ihr neues Passwort lautet:", genPW)
else:
    quit("°_°")

laenge = int(input("Wie lang soll das Passwort sein?: "))
alleZeichen = [grossbuchstabe, kleinbuchstabe, sonderzeichen, ziffer]

genPW = len(laenge) + alleZeichen

