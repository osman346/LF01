picture = [["-", "o", "o", "o", "o", "-", "-", "-"],
           ["-", "o", "-", "-", "-", "o", "-", "-"],
           ["-", "o", "-", "-", "-", "o", "-", "-"],
           ["-", "o", "o", "o", "o", "-", "-", "-"],
           ["-", "o", "o", "-", "-", "-", "-", "-"],
           ["-", "o", "-", "o", "-", "-", "-", "-"],
           ["-", "o", "-", "-", "o", "-", "-", "-"],
           ["-", "o", "-", "-", "-", "o", "-", "-"]]


def verarbeitung(reihe, picture, zeichen):
    for reihe in picture:
        for zeichen in reihe:
            print(zeichen, end="")
        print()
    return reihe
    return picture
    return zeichen

print()
print("horizontal")
print()

verarbeitung(reihe, picture, zeichen)

print()
print("vertikal")
print()

for reihe in picture:
    for zeichen in reihe[::-1]:
        print(zeichen, end="")
    print()

print()
print("90°")
print()

for i in range(len(picture[0])):
    for j in range(len(picture)):
        print(picture[-1-j][i], end="")
    print()


print()
print("180°")
print()

for reihe in picture[::-1]:
    for zeichen in reihe[::-1]:
        print(zeichen, end="")
    print()

print()
print("270°")
print()

for i in range(len(picture[0])):
    for j in range(len(picture)):
        print(picture[j][-1-i], end="")
    print()
