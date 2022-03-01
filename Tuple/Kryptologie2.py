matrix = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "BCDEFGHIJKLMNOPQRSTUVWXYZA",
          "CDEFGHIJKLMNOPQRSTUVWXYZAB",
          "DEFGHIJKLMNOPQRSTUVWXYZABC",
          "EFGHIJKLMNOPQRSTUVWXYZABCD",
          "FGHIJKLMNOPQRSTUVWXYZABCDE",
          "GHIJKLMNOPQRSTUVWXYZABCDEF",
          "HIJKLMNOPQRSTUVWXYZABCDEFG",
          "IJKLMNOPQRSTUVWXYZABCDEFGH",
          "JKLMNOPQRSTUVWXYZABCDEFGHI",
          "KLMNOPQRSTUVWXYZABCDEFGHIJ",
          "LMNOPQRSTUVWXYZABCDEFGHIJK",
          "MNOPQRSTUVWXYZABCDEFGHIJKL",
          "NOPQRSTUVWXYZABCDEFGHIJKLM",
          "OPQRSTUVWXYZABCDEFGHIJKLMN",
          "PQRSTUVWXYZABCDEFGHIJKLMNO",
          "QRSTUVWXYZABCDEFGHIJKLMNOP",
          "RSTUVWXYZABCDEFGHIJKLMNOPQ",
          "STUVWXYZABCDEFGHIJKLMNOPQR",
          "TUVWXYZABCDEFGHIJKLMNOPQRS",
          "UVWXYZABCDEFGHIJKLMNOPQRST",
          "VWXYZABCDEFGHIJKLMNOPQRSTU",
          "WXYZABCDEFGHIJKLMNOPQRSTUV",
          "XYZABCDEFGHIJKLMNOPQRSTUVW",
          "YZABCDEFGHIJKLMNOPQRSTUVWX",
          "ZABCDEFGHIJKLMNOPQRSTUVWXY")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

liste = []

while True:
    modus = input("Willkommen, was wollen Sie tun?\n| A | Entschlüsseln"
                  " | B | Verschlüsseln : ")
    if modus == "A" or modus == "a":
        eingabe = input("Bitte geben Sie ein Wort ein: ")
        for i in range(0, len(eingabe)):
            wortstelle = eingabe[i]
            liste.append(*[wortstelle])
        key = input("Bitte nennen Sie den Schlüssel: ")
        for i in range(0, len(eingabe)):
            mathe = liste[i]
            k = key[i % len(key)]
            eingabeindex = alphabet.index(mathe.upper())
            keyindex = alphabet.index(k.upper())
            liste[i] = matrix[keyindex][eingabeindex]
        print("Code-Wort:", *liste, sep="")
        quit()
        #   Verschlüsselung
    elif modus == "B" or modus == "b":
        eingabe = input("Bitte geben Sie Code-Wort ein: ")
        for i in range(0, len(liste)):
            print("a")
