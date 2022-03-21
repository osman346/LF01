import random
import string


def welcome():
    print("Willkommen beim Chatbot!")


name = input("Wie ist Ihr Name: ")


def namen_abfrage():
    print("Willkommen", name)


def benutzeranleitung():
    print(name, ",", "Wenn du Hilfe benötigst hier:")
    print("Beenden  | Zum beenden musst du einfach 'bye' eintippen")
    print("Frage    | Zum fragen musst du einfach 'frage' eintippen")
    print("Leer     | Zum wiederholen der Eingabe musst du einfach nichts eintippen")
    print("Hilfe    | Für Hilfe  musst du einfach 'hilfe' eintippen")


zufallsantworten = ["Weiß ich nicht...", "Leider kann ich dir das nicht beantworten ", "Interesannt... "
                                                                                        "Kannst du das anders formulieren?",
                    "Das habe ich leider nicht verstanden..."]

welcome()  # Willkommens Text
namen_abfrage()  # Name wird gedruckt
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
        print(random.choice(zufallsantworten))
    elif eingabe == "" or eingabe == " ":
        optionen = input("Ungültige Eingabe - Sie haben zwei Möglichkeiten\n1. Frage oder 2. Benutzeranleitung\n")
        if optionen == "1":
            thema = input("Worüber möchtest du heute sprechen?\n")
            thema = thema.lower()
            thema = thema.split()
            print(random.choice(zufallsantworten))
        elif optionen == "2":
            benutzeranleitung()
        else:
            print("Ungültige Eingabe!")
    elif eingabe == "bye" or eingabe == "Bye" or eingabe == "Bye!" or eingabe == "bye!":
        quit("Exiting...")