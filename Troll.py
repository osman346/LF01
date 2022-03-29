def trollmathematik(troll):
    zahl = troll / 4
    zahl = int(zahl)
    for i in range(zahl):
        print("viele", end=" ")
    troll %= 4
    print(troll)
    return troll, zahl


def dezimalmathematik(dezimal):
    zahl = dezimal * 4
    zahl = int(zahl)
    for i in range(zahl):
        print(zahl, end=" ")
    dezimal /= 4
    print(dezimal)
    return dezimal, zahl


auswahl = input("1. | Troll in Dezimal\n"
                "2. | Dezimal in Troll\n")

if auswahl == "1" or auswahl == "Troll in Dezimal":
    troll = int(input("Nenne mir eine Dezimal Zahl: "))
    trollmathematik(troll)
elif auswahl == "2" or auswahl == "Dezimal in Troll":
    dezimal = input("Nenne mir eine Troll Zahl: ")
    dezimalmathematik(dezimal)