kredit = int(input("Wie viel Geld möchten Sie in € leihen?\n"))
zinssatz = float(input("Nennen Sie mir ihren jährlichen Zinssatz in %\n"))
rueckzahlung = kredit * zinssatz / 100 + kredit
tilgung = kredit * zinssatz / 100 + kredit
print("Sie sind ihrer Bank bei einem Zinssatz von", float(zinssatz), "%")
print("und einem Kredit von", kredit, "€")
print(tilgung, "€", "Schuldig.")