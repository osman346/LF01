#   Aufgabe 1

k = 1
s = 0

for i in range(1000000):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k
    k += 2

print("Aufgabe 1", s)
print()
print("Aufgabe 2")
#   Aufgabe 2

for x in range(64):
    print(2 ** x)
print()
print("Aufgabe 3")
#   Aufgabe 3

print("Jahr     Anfangspopulation    Zuwachs    Endpopulation")
jahr = 2000                 # Jahr
anfangspopulation = 6.125   # Anfangspopulation
zuwachs = 0.092             # Zuwachs
endpopulation = 6.217       # Endpopulation
stern = ""                  # Stern

weiter = "j"

while weiter == "j" or weiter == "J":
    for i in range(5):
        print(f"{jahr}{stern}            {round(anfangspopulation, 3):=10}{round(zuwachs, 3):=10}       {round(endpopulation, 3):=10}")
        anfangspopulation = endpopulation
        endpopulation = endpopulation / 100 * 1.5
        endpopulation = anfangspopulation + endpopulation
        jahr += 1
        zuwachs = endpopulation - anfangspopulation
        if jahr >= 2013:
            stern = "*"

    weiter = input('Weiter? (J/N)')

#   Aufgabe 4

for i in range(0, 7):
    for j in range(0, 7):
        print(f"({i}", "|",  f"{j})", end=" ")
        if i == 0 and j == 6:
            print("\n")
        if i == 1 and j == 6:
            print("\n")
        if i == 2 and j == 6:
            print("\n")
        if i == 3 and j == 6:
            print("\n")
        if i == 4 and j == 6:
            print("\n")
        if i == 5 and j == 6:
            print("\n")
        if i == 6 and j == 6:
            print("\n")
