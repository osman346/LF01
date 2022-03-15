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
new_list = []
while True:
    modus = input("Willkommen, was wollen Sie tun?\n| A | Entschlüsseln"
                  " | B | Verschlüsseln : ")
    if modus == "A" or modus == "a":
        eingabe1 = input("Bitte geben Sie Code-Wort ein: ")
        keyE = input("Bitte nennen Sie den Schlüssel: ")

        for i in range(len(eingabe1)):
            index_text = alphabet.index(eingabe1[i])
            if i >= len(keyE):
                keyE += keyE
            index_key = alphabet.index(keyE[i])
            index_neu = (index_text - index_key)
            if index_neu >= 26:
                index_neu = index_neu - 26
            letters_neu = alphabet[index_neu]
            new_list.append(letters_neu)
        print("".join(new_list))
        quit()
        new_list.clear()
    elif modus == "B" or modus == "b":
        eingabe = input("Bitte geben Sie Code-Wort ein: ")
        for i in range(0, len(eingabe)):
            wortstelle = eingabe[i]
            liste.append(*[wortstelle])
        keyE = input("Bitte nennen Sie den Schlüssel: ")
        for i in range(0, len(eingabe)):
            mathe = liste[i]
            k = keyE[i % len(keyE)]
            eingabeindex = alphabet.index(mathe.upper())
            keyindex = alphabet.index(k.upper())
            liste[i] = matrix[keyindex][eingabeindex]
        print("Wort:", *liste, sep="")
        quit()
