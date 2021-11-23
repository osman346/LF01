import time
# Aufgabe 1
name = input("Wie heißen Sie?\n")
print("Hallo", name)
# Aufgabe 2
team1 = input("Wie heißt Team 1?\n")
team2 = input("Wie heißt Team 2?\n")
print(team1, "vs.", team2, "heute Abend um 19.00 UHR")
# Aufgabe 3
time.sleep(2)
zahl = int(input("Wie viele Packungen Popcorn möchten sie Kaufen?\n"))
print("Das macht dann", zahl * 2, "€")
# Aufgabe 4
team1p = int(input("Wie viele Punkte hat Team 1 erzielt?\n"))
team2p = int(input("Wie viele Punkte hat Team 2 erzielt?\n"))
print("Ergebnis:", team1, team1p, ":", team2, team2p)
# Aufgabe 5 + Extra
time.sleep(2)
print("Willkommen bei der Rechtecksberechnung!")
a = float(input("Wie lang ist Seite a in Centimeter?\n"))
b = float(input("Wie lang ist Seite b in Centimeter?\n"))
Umfang = (2 * a + 2 * b)
FI = (a * b)
Diagonale = (a ** 2 + b ** 2)
print("Umfang:", Umfang, "Flaecheninhalt:", FI, "Diagonale:", Diagonale, sep="\n")