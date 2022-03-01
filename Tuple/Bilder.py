#   Aufgabe 1
zeile1 = ["-", "o", "o", "o", "o", "-", "-", "-"]
zeile2 = ["-", "o", "-", "-", "-", "o", "-", "-"]
zeile3 = ["-", "o", "-", "-", "-", "o", "-", "-"]
zeile4 = ["-", "o", "o", "o", "o", "-", "-", "-"]
zeile5 = ["-", "o", "o", "-", "-", "-", "-", "-"]
zeile6 = ["-", "o", "-", "o", "-", "-", "-", "-"]
zeile7 = ["-", "o", "-", "-", "o", "-", "-", "-"]
zeile8 = ["-", "o", "-", "-", "-", "o", "-", "-"]
aeussere_liste = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8]
#   Aufgabe 2
x = 0
for i in range(1, 9):
    print(*aeussere_liste[x], sep="")
    x += 1
print("Vertikal")
x = 7
for i in range(1, 9):
    print(*aeussere_liste[x], sep="")
    x -= 1
print("Auf dem Kopf")
for i in range(8):
    for b in reversed(range(8)):
        print(aeussere_liste[i][b], end="")
    print("")
print("Horizontal")
#   Aufgabe 3
print("90°")
for i in range(8):  # 90 Grad
    for b in reversed(range(8)):
        print(aeussere_liste[b][i], end="")
    print("")
print("180°")
for i in reversed(range(8)):
    for b in reversed(range(8)):
        print(aeussere_liste[i][b], end="")
    print("")
print("270°")
for b in reversed(range(8)):
    for i in range(8):
        print(aeussere_liste[i][b], end="")
    print("")
