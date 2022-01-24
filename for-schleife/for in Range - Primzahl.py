#   https://www.delftstack.com/de/howto/python/python-isprime/

#Primzahltest

eingabe = int(input("Zahl eingeben:\n"))

if eingabe > 1:
    for i in range(2, int(eingabe / 2) + 1):
         if (eingabe % i) == 0:
            print("Es ist keine Primzahl")
            break
    else:
        print("Es ist eine Primzahl")
else:
    print("Es ist keine Primzahl")


#Primzahlfunktion

