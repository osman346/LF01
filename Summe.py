def input_integer():
    anfang = input("Nennen Sie den Summenanfang: ")
    while not anfang.isdigit():
        anfang = input("Nennen Sie den Summenanfang: ")
    anfang = int(anfang)
    return anfang


def ende_funktion():
    ende = input("Nennen Sie das Summenende: ")
    while not ende.isdigit():
        ende = input("Nennen Sie das Summenende: ")
    ende = int(ende)
    return ende


def verarbeitung(anfang, ende):
    summe = ende
    for i in range(anfang, ende):
        summe += i
    return summe


def summe_berechnen(anfang, ende, summe):
    print("Die Summe der Zahlen von " + str(anfang) + " bis " + str(ende) + " lautet: " + str(summe))


a = input_integer()
b = ende_funktion()
c = verarbeitung(a, b)
summe_berechnen(a, b, c)
