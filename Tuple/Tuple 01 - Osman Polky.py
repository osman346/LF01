import random

#   Aufgabe 1
karten = ("Ass", "König", "Dame", "Bube", "Zehn", "Neun", "Acht", "Sieben")
farben = ("Kreuz", "Pik", "Herz", "Karo")
liste = []
for i in farben:
    for q in karten:
        liste.append((i, q))
print(liste[0], liste[-1])
print(liste)
print("-------------------------------------------------------")
#   Aufgabe 2
while True:
    pos = int(input("Bitte geben Sie eine Position ein: "))
    pos2 = int(input("Bitte geben Sie eine weitere Position ein: "))

    print("Vorher:", liste[pos], liste[pos2])

    a = int(pos)
    b = int(pos2)

    liste[a], liste[b] = liste[b], liste[a]
    print("Nachher:", liste[a], liste[b])
    print("Gemischtes Deck:", liste)
    weiter = input("Weiter machen? (J/N): ")
    if weiter == "Nein" or weiter == "nein" or weiter == "n" or weiter == "N":
        break
print("-------------------------------------------------------")
#Aufgabe 3: Zufälliges mischen.
zufallszahl = 0
zufallszahl2 = 0
wiederholung = 0
print("Aufgabe 3: Zufälliges mischen.")


while wiederholung != 100:
    wiederholung+=1
    for i in range (100):

        zufallszahl = random.randint(1, 31)
        zufallszahl2 = random.randint(1, 31)

    n1 = int(zufallszahl)
    n2 = int(zufallszahl2)

    print("Karte", n1, ":", liste[n1])
    print("wird mit")
    print("Karte", n2, ":", liste[n2], )
    print("getauscht", "\n")

    liste[n1], liste[n2] = liste[n2], liste[n1]

print("Zufällig gemischte Karten:",liste)
