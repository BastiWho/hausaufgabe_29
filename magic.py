print("Zahlenrätsel")
print("============")

import random

versuch = 0
ratezahl = random.randint(0,9)

while True:
    versuch = versuch + 1
    benutzerzahl = int(input("Bitte gib eine Zahl zwisch 0 und 9 ein: "))
    print("\n" + str(versuch)+". Versuch.\0")
    if benutzerzahl == ratezahl:
        print("Das war korrekt! Du hast die richtige Zahl eingetippt\n")
        print("Du hast " +str(versuch)+ " Versuch(e) benötigt, um das Spiel zu gewinnen!")
        print("====================")
        print("Ende des Spiels")
        break
    elif benutzerzahl >= ratezahl:
        print("Deine Einabe war zu groß.\n")
    else:
        print("Die Zahl war zu klein.\n")

