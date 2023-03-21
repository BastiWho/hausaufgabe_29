print("Bitte gib einen Satz ein, um die darin befindlichen Vokale zu zählen: \n")

vokale = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
zaehlen = 0
satz = input()

for i in satz:
    if i in vokale:
        zaehlen = zaehlen + 1
print("In deinem Satz waren " + str(zaehlen) + " Vokale")

datei = open("Anzahl_Vokale.txt", "w")
text = ("In deinem Satz waren " + str(zaehlen) + " Vokale")
datei.write (text)

print("Die Anzahl der Vokale wurde in die Datei Anzahl_Vokale.txt geschrieben")