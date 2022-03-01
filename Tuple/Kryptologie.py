alphabet = 'abcdefghijklmnopqrstuvwxyz'
while True:
    modus = input("Willkommen, was wollen Sie tun?\n| A | Entschlüsseln"
                  " | B | Verschlüsseln : ")
    if modus == "A" or modus == "a":
        txt = str(input("Verschlüsselter Text: "))
        schlussel = int(input("Wie groß ist die Verschiebung? "))
        txt = txt.lower()
        geheimtext = ""
        for buchstabe in txt:
            if buchstabe == " ":
                geheimtext += " "
            else:
                nummer = alphabet.index(buchstabe)
                nummer -= schlussel
                if nummer < 0:
                    nummer += 26
            geheimtext += alphabet[nummer]
        print("Geheimtext:", geheimtext.upper())
        quit()
    elif modus == "B" or modus == "b":
        txtE = str(input("Entschlüsselter Text: "))
        schlussel = int(input("Wie groß ist die Verschiebung? "))
        txtE = txtE.lower()
        geheimtext = ""
        for buchstabe in txtE:
            if buchstabe == " ":
                geheimtext += " "
            else:
                nummer = alphabet.index(buchstabe)
                nummer += schlussel
                if nummer > 25:
                    nummer -= 26
            geheimtext += alphabet[nummer]
        print("Geheimtext:", geheimtext.upper())
        quit()
