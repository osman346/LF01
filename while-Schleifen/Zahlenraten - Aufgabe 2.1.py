import random

versuche = 0
True1 = True
zahl = random.randint(50, 100)

while True:
    versuche += 1
    print("Ihr", versuche, "Versuch.")
    eingabe = int(input("Nennen Sie mir eine Zahl \n"))

    if eingabe == zahl:
        print("Richtig erraten \n")
        True1 = False
        break
    elif eingabe > zahl:
        print("die geratene Zahl ist zu groß")
    else:
        print("die geratene Zahl ist zu klein_buchstaben")

    if (versuche == 7):
        print("zu oft falsch, neuer Versuch.")
        print("Die Zahl war " + str(zahl))
        True1 = False
print("Glückwunsch, Ende.")

