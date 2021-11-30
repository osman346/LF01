tip1 = int(input("Heim: Wie viel tippen Sie?\n"))
tip2 = int(input("Auswaerts: Wie viel tippen Sie?\n"))
tip3 = int(input("Heim: Tore\n"))
tip4 = int(input("Auswaerts: Tore\n"))

punkte = 1

if tip1 == tip3:
    punkte += 1
elif tip1 != tip3:
    punkte -= 1

if tip2 == tip4:
    punkte += 1
elif tip2 != tip4:
    punkte -= 1

if punkte == -1:
    punkte += 1

print("Ergebnis:", ",", tip3, ":", tip4, "Tipp:", tip1, ":", tip2, ",", "->", punkte)

