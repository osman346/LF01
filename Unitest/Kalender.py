import math

# Input
Monat = input("Wählen Sie bitte einen Monat aus (negative Werte werden nicht geduldet).\n")
# Eingabeüberprüfung
while True:
    if not int(
            Monat.isdecimal()):  # Wenn der Monat keine Dezimal Zahl ist wird erneut nach einer Zahl zwischen 1-12
        # gefragt.
        Monat = input("Bitte nennen Sie keine Zeichenkette oder negative Werte. (1-12)\n")
    elif int(Monat) >= 13 or int(
            Monat) <= 0:  # Die Eingabe von Monat wird hier umgewandelt in einen Integer und es findet eine Abfrage
        # statt.
        Monat = input("Bitte nennen Sie eine korrekte Zahl. (1-12)\n")
    else:
        Monat = int(Monat)
        break
# Input
Jahr = input("Wählen Sie bitte eine Jahr aus (negative Werte werden nicht geduldet).\n")
# Eingabeüberprüfung
while True:
    if not int(Jahr.isdecimal()):  # Wenn das Jahr keine Dezimal Zahl ist wird erneut nach einer Zahl zwischen 0-X
        # gefragt.
        Jahr = input("Bitte nennen Sie keine Zeichenkette oder negative Werte. (0-X)\n")
    elif int(Jahr) < 0:  # Die Eingabe von Jahr wird hier umgewandelt in einen Integer und es findet eine Abfrage statt.
        Jahr = input("Bitte nennen Sie eine korrekte Zahl. (0-X)\n")
    else:
        Jahr = int(Jahr)
        break
# Schaltjahr Berechnung
if Jahr % 4:
    print("Es handelt sich nicht um ein Schaltjahr.")
    februar = 1  # Februar hat 28. Tage
else:
    print("Es handelt sich um ein Schaltjahr.")
    februar = 0  # Februar hat 29. Tage
# Wochentagesbestimmung # Quelle: https://de.wikipedia.org/wiki/Wochentagsberechnung#Programmierung
tag = 1
if Jahr < 3:
    Jahr = Jahr - 1
wochen_tag = ((tag + math.floor(2.6 * ((Monat + 9) % 12 + 1) - 0.2) + Jahr % 100 + math.floor(
    Jahr % 100 / 4) + math.floor(Jahr / 400) - 2 * math.floor(Jahr / 100) - 1) % 7 + 7) % 7 + 1
print("Wochentag:", wochen_tag)  # Der erste Tag im Monat  Wochentag Bsp. Mittwoch ist der 01.12.2021
# Bestimmung der maximalen Tage im Monat
if Monat == 1 or Monat == 3 or Monat == 5 or Monat == 7 or Monat == 8 or Monat == 10 or Monat == 12:
    print("Dieser Monat hat 31 Tage.")
if Monat == 2 and februar == 1:
    print("Dieser Monat hat 28 Tage.")
elif Monat == 2 and februar == 0:
    print("Dieser Monat hat 29 Tage.")
if Monat == 4 or Monat == 6 or Monat == 9 or Monat == 11:
    print("Dieser Monat hat 30 Tage.")
# Ausgabe
print('Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So')
br = 1  # Damit die Zahlen ab Sonntag eine Zeile brechen
if Monat == 1 or Monat == 3 or Monat == 5 or Monat == 7 or Monat == 8 or Monat == 10 or Monat == 12:
    for zahl in range(1, 32):
        if br == 7:
            print(f"{zahl:>2}", sep="\n")
            br = 0
        else:
            print(f"{zahl:>2}", end=" ")  # Das String Formatting hilt damit die Zahlen sauber unter den Wochentagen
            # stehen. Emre, Frau Naber und "Python String Formatting.pdf" haben mir auf die Sprünge geholfen.
        br += 1
if Monat == 2 and februar == 1:
    for zahl in range(1, 29):
        if br == 7:
            print(f"{zahl:>2}", sep="\n")
            br = 0
        else:
            print(f"{zahl:>2}", end=" ")
        br += 1
elif Monat == 2 and februar == 0:
    for zahl in range(1, 30):
        if br == 7:
            print(f"{zahl:>2}", sep="\n")
            br = 0
        else:
            print(f"{zahl:>2}", end=" ")
        br += 1
if Monat == 4 or Monat == 6 or Monat == 9 or Monat == 11:
    for zahl in range(1, 31):
        if br == 7:
            print(f"{zahl:>2}", sep="\n")
            br = 0
        else:
            print(f"{zahl:>2}", end=" ")
        br += 1
