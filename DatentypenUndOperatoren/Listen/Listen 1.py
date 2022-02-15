print("Aufgabe 1")
liste = [1, 2, 3]
i = 0
while i < len(liste):
    print(liste[i])
    i += 1
print("Die Länge der Liste:", len(liste))
print("")

print("Aufgabe 2")
print(liste[0], liste[1], liste[2])
print("")

print("Aufgabe 3")
for q in liste:
    print(q)
print("")

print("Aufgabe 4")
for i in range(1):
    print(liste[0], liste[1], liste[2])
print("")

print("Aufgabe 5")
for i in liste[::-1]:
    print(i)

#   zweite Lösunng
#   while f <= len(liste):
#     print(liste[-f])
#     f += 1

print("")
print("Aufgabe 6")
listex = [1, 2, 3, 4, 5]
summe = 0
for t in range(len(listex)):
    summe += listex[t]
print(summe)

print("")
print("Aufgabe 7")

leerliste = []
for u in range(1, 9):
    u *= u
    leerliste.append(u)
print(leerliste)

print("")
print("Aufgabe 8")

liste3 = [1, 2, 3]
liste4 = [4, 5, 6]
liste3.extend(liste4)
print(liste3)

print("")
print("Aufgabe 9")

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste1.append(liste2)
print(liste1)

print("")
print("Aufgabe 10")

liste10 = [1, 2, 3, 4, 5]
print("Vorher:", liste10)
liste10.remove(2)
print("Nachher:", liste10)

#   credits osman346
