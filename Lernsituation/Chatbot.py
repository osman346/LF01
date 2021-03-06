import random


def welcome():
    print("Willkommen beim Chatbot!")


name = input("Wie ist Ihr Name: ")


def namen_abfrage():
    print("Willkommen", name)


def benutzeranleitung():
    print(name, ",", "wenn du Hilfe benötigst hier:")
    print("Beenden  | Zum beenden musst du einfach 'bye' eintippen")
    print("Frage    | Zum fragen musst du einfach 'frage' eintippen")
    print("Hilfe    | Für Hilfe musst du einfach 'hilfe' eintippen")


zufallsantworten = ["Weiß ich nicht...", "Leider kann ich dir das nicht beantworten ", "Interesannt... "
                                                                                        "Kannst du das anders "
                                                                                        "formulieren?",
                    "Das habe ich leider nicht verstanden..."]
antworten = {"strom": "Ich liebe Strom!",
             "bist du": "Ich bin eine KI",
             "hallo": "Hi!",
             "dich" and "programmiert": "Mein programmierer heißt Osman",
             "entsperre" and "account": "Melde dich hierfür bitte beim Support Level '2'",
             "wie lange" and "unternehmen": "Unser Unternehmen gibt es seit ca. 5 Jahren",
             "bye": "Tschüss! ich hoffe ich konnte dir weiterhelfen",
             "alt": "Ich bin drei Wochen alt"}


def passende_antworten():
    for i in thema:
        if i in antworten.keys():
            print(antworten[i])
            break
    else:
        print(random.choice(zufallsantworten))


welcome()  # Willkommens Text
namen_abfrage()  # Name wird gefragt
print("")
benutzeranleitung()  # Benutzeranleitung
print("")

while True:
    eingabe = input("Bitte gebe etwas ein: ")
    if eingabe == "hilfe" or eingabe == "Hilfe":
        benutzeranleitung()
    elif eingabe == "frage" or eingabe == "Frage":
        thema = input("Worüber möchtest du heute sprechen?: ")
        thema = thema.lower()
        thema = thema.split()
        passende_antworten()
    elif eingabe == "" or eingabe == " ":
        optionen = input("Ungültige Eingabe - Sie haben zwei Möglichkeiten\n1. Frage oder 2. Benutzeranleitung\n")
        if optionen == "1":
            thema = input("Worüber möchtest du heute sprechen?\n")
            thema = thema.lower()
            thema = thema.split()
            passende_antworten()
        elif optionen == "2":
            benutzeranleitung()
        else:
            print("Ungültige Eingabe!")
    elif eingabe == "bye" or eingabe == "Bye" or eingabe == "Bye!" or eingabe == "bye!":
        quit("Exiting...")
    else:
        print("Ungültige Eingabe!")
