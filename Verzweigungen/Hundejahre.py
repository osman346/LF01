# Allgemeine Methode

print("Wie alt ist ihr Hund?")
alter = int(input())

print("Ihr Hund wäre", alter * 7, "Jahre alt wäre er ein Mensch")

# Spezielle Methode

print("Wie alt ist ihr Hund?")
alter2 = int(input())

if alter2 == 1:
    print("Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.")
elif alter2 == 2:
    print("Ein zweijähriger Hund entspricht in etwa einem 22-jährigen Menschen.")
elif alter2 > 2:
    print("Ein", alter2, "jähriger Hund entspricht in etwa einem", (alter2 + 1) * 7 -1, "Jährigen Menschen")