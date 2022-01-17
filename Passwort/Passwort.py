import string
import random
from colorama import Fore

#  Eingabe
passwort = input("Geben Sie bitte ein Passwort ein.\n")
sicherheitsstufe = 0

#  Besitzt das Passwort Sonderzeichen, Großbuchstaben, Kleinbuchstaben und Ziffern?
sonderzeichen = ['!', '§', '$', '%', '&', '/', '(', ')', '=', '?', 'ß', "'", '"', '*', '#', '.', '_', '-', ';', ',',
                 '~', '+', ']', '[', '}', '{', '<', '>', '|', '@', '^', '°', ':', '€', 'µ', '´', '`', ' ']

for a in sonderzeichen:
    if a in passwort:
        sicherheitsstufe += 1
        break

grossbuchstabe = string.ascii_uppercase  # Beinhaltet alle Großenbuchstaben.
for b in grossbuchstabe:
    if b in passwort:
        sicherheitsstufe += 1
        break

kleinbuchstabe = string.ascii_lowercase  # Beinhaltet alle Kleinenbuchstaben.
for c in kleinbuchstabe:
    if c in passwort:
        sicherheitsstufe += 1
        break

ziffer = string.digits  # Beinhaltet alle Zahlen.
for d in ziffer:
    if d in passwort:
        sicherheitsstufe += 1
        break

#  Passwort Länge
if len(passwort) >= 10:
    sicherheitsstufe += 1
else:
    print(Fore.RED + "Ihr Passwort beinhaltet keine 10 Zeichen.")
    sicherheitsstufe -= 1

#  Übeprüfung, welchen Wert der Status hat
if sicherheitsstufe == 5:
    print(Fore.CYAN + "Ihr Passwort ist stark.")
elif sicherheitsstufe == 3 or sicherheitsstufe == 4:
    print(Fore.GREEN + "Ihr Passwort ist gut.")
elif sicherheitsstufe == 2:
    print(Fore.YELLOW + "Ihr Passwort ist okay.")
elif sicherheitsstufe == 1:
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
print("------------------------------------------------------")
gen = input("Möchten Sie ein Passwort generieren? (J/N)\n")


def genpw():  # Passwort generierung
    zeichen = grossbuchstabe + kleinbuchstabe + ziffer + string.punctuation
    return ''.join(random.choice(zeichen) for _ in range(laenge))


if gen == "J" or gen == "j":  # Abfrage für ein neues Passwort
    print("Ihr neues Passwort lautet:", genpw())
    laenge = int(input("Wie lang soll das Passwort sein?: "))
else:
    quit("Sie entschieden sich dafür kein Passwort zu generieren.")
