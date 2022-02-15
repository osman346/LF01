import random

liste = []
for i in range(0, 20):
    wert = random.randint(0, 100)
    liste.append(wert)
print("Liste:", liste)

tuple(liste)

b = sum(liste) / len(liste)
print("Mittelwert:", b)
print("Median:", liste[9] + liste[10] / 2)

varianz = 0
for i in liste:
    varianz += (i - b) ** 2
varianz /= len(liste)

standardabweichung = varianz ** 0.5
print(liste)
