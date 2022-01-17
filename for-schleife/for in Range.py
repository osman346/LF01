for i in range (6):
print(i)
for a in range (2,8):
print(a)
for b in range (1, 20, 2):
print(b)
for c in range (10, -12, -2):
print(c)


while True:
    for abfrage in range(1):
        zahl = input("Geben Sie eine Zahl ein\n")

        if int(zahl) % 7:
            print("Ist nicht teilbar.")
        elif zahl == " ":
            break
        else:
            print("Ist teilbar.")

x = 0
y = 0
for y in range(1, 4):
    for x in range(1, 6):
        print(y * x, end=" ")
    print(" ")
