#Aufgabe Leonardo Fibonacci

bedingungen = int(input("Wie viele Stellen?\n"))

bedingung1 = 0
bedingung2 = 0
zaehler = 0

if bedingungen <= 0:
   print("Bitte eine positive Zahl eingeben")
elif bedingungen == 1:
   print("Fibonacci", bedingungen, ":")
   print(bedingung1)
else:
   print("Fibonacci:")
   while zaehler < bedingungen:
       print(bedingung1)
       bedigung1und2 = bedingung1 + bedingung2
       bedingung1 = bedingung2
       bedingung2 = bedigung1und2
       zaehler += 1

