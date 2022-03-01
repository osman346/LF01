# Aufgabe 1
print("Aufgabe 1:", "Drücken Sie 'ENTER' um die Liste rückwärts anzuzeigen")
eingabe = 0
liste1 = []
liste2 = []

while True:
    eingabe = input("Schreiben sie ein Wort: ")
    if eingabe == "" or eingabe == " ":
        print("Liste Vorwärts:", liste1, )
        liste2.extend(liste1)
        liste2.reverse()
        print("Liste Rückwärts:", liste2)
        break
    else:
        liste1.append(eingabe)
        print(liste1)

# Aufgabe 2
print("Aufgabe2:")

liste = []
liste2 = []

anzahl = int(input("Wie viele Elemente?"))

for i in range(0, anzahl):
    eingabe = input("Schreiben sie ein Wort (Liste 1): ")
    liste.append(eingabe)
anzahl2 = int(input("Wie viele Elemente?"))

for i in range(0, anzahl2):
    eingabe = input("Schreiben sie ein Wort (Liste 2): ")
    liste2.append(eingabe)

while True:
    auswahl = input(" a) Liste anzeigen\n b) Listenelemente hinten einfügen\n c) Listenelement an einer bestimmten Stelle "
                "einf"
                "ügen\n d) Listenelement löschen\n e) Suchen (Vorhandensein bestätigen und Index eines Elementes aus"
                "geben)\n")

    if auswahl == "a":
        print(liste)
    elif auswahl == "b":
        liste.extend(liste2)
        print(liste)
    elif auswahl == "c":
        einfg = int(input("Wo möchten Sie die zweite Liste einfügen?"))
        liste.insert(einfg, liste2)
        print(liste)
    elif auswahl == "d":
        losch = input("Wo möchten Sie das Element löschen?")
        liste.remove(losch)
        print(liste)
    elif auswahl == "e":
        pruf = input("Überprufen von Element ?")
        check = pruf in liste
        if check == True:
            print("Existiert")
        elif check == False:
            print("Existiert nicht")
    elif auswahl != "a" or auswahl != "b" or auswahl != "b" or auswahl != "c" or auswahl != "d" or auswahl != "e":
        print("Programm wird beendet")
        break