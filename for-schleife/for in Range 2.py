#Aufgabe 1

k = 1
stern = 0

for i in range(1000000):
    if i % 2 == 0:
        stern += 4 / k
    else:

        stern -= 4 / k

    k += 2

print("Aufgabe 1", stern)

#Aufgabe 2

anfangspopulation= 0

for anfangspopulation in range(64):
    print(2 ** anfangspopulation)

#Aufgabe 3

print("Jahr     Anfangspopulation    Zuwachs    Endpopulation")
jahr = 2000                 # Jahr
anfangspopulation = 6.125   # Anfangspopulation
zuwachs = 0.092                   # Zuwachs
endpopulation = 6.217       # Endpopulation
stern = ""                  # Stern

weiter = "j"

while weiter == "j" or weiter == "J":
    for i in range(5):
        print(f"{jahr}{stern}        {round(anfangspopulation, 3):=10}                {round(zuwachs, 3):=10}      {round(endpopulation, 3):=10}")
        anfangspopulation = endpopulation
        ep = endpopulation / 100 * 1.5
        endpopulation = ep + endpopulation
        jahr += 1
        zuwachs = endpopulation - anfangspopulation
        if jahr >= 2013:
            stern = "*"

    weiter = input('Weiter Machen? Für Ja "J" eingeben.')