aussere_liste = []
for i in range(1, 11):
    string = " "
    innere_liste = []
    for j in range(1, 11):
        string = string + str(i * j) + '\t'
        innere_liste.append(i * j)
    aussere_liste.append(innere_liste)
print(aussere_liste)

zahl1 = int(input("Nennen Sie eine Zahl: "))
zahl2 = int(input("Nennen Sie noch eine Zahl: "))
print("Ergebniss:", aussere_liste[zahl1 - 1][zahl2 - 1])

