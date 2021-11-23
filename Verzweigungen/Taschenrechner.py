a = int(input("Nennen Sie mir eine Zahl.\n"))
r = input("Mit was wird gerechnet?\n")
b = int(input("Nennen Sie mir die zweite Zahl.\n"))

#if r == ":" and b == 0:
 #   print("Mit '0' kann ich leider nicht teilen ;(")
  #  exit()
    
if r != "+" and r != "-" and r != ":" and r != "*":
    print("Sie müsssen ein gültiges Rechenzeichen eingeben.")
elif r == "+":
    print("Das Ergebnis lautet:", a, r, b,"=", a+b)
elif r == "-":
    print("Das Ergebnis lautet:", a, r, b,"=", a-b)
elif r == ":":
    if b == 0:
        print("Mit '0' kann ich leider nicht teilen ;(")
    else:
        print("Das Ergebnis lautet:", a, r, b,"=", a/b)
elif r == "*":
    print("Das Ergebnis lautet:", a, r, b,"=", a*b)

    