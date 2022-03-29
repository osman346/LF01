def frage():
    zahl1 = int(input("Bitte nennen Sie eine Zahl"))
    zahl2 = int(input("Bitte nennen Sie eine Zahl"))
    int(zahl1)
    int(zahl2)
    return zahl1, zahl2


def mittelwert(zahl1, zahl2):
    print("Mittelwert:", (zahl1 + zahl2) / 2)
    return zahl1, zahl2


def max(zahl1, zahl2):
    print("Das Maxiumum:", (zahl1 + zahl2))
    return zahl1, zahl2


def min(zahl1, zahl2):
    print("Das Minimum:", (zahl1 - zahl2))
    return zahl1, zahl2


def abstand(zahl1, zahl2):
    print("Der absolute Abstand:", (zahl1 - zahl2))
    return zahl1, zahl2


a = frage()
b = mittelwert()
c = max()
d = min()
e = abstand()
