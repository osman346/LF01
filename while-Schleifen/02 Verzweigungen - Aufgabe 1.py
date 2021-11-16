alter = int(input("Wie alt sind Sie? \n"))
if 14 <= alter <= 17:
    print("Sie sind Jugendlich.")
elif alter <= 14:
    print("Beurteilung nicht möglich, zu jung.")
else:
    print("Sie sind Erwachsen.")
