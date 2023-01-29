seznam = []

with open("01_data.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        #print(radek) 
        seznam.append(radek)


print(seznam)
delka_seznamu = len(seznam)
soucet_cisel = 0
seznam_souctu = []

for prvek in range(delka_seznamu):
    delka_prvku = len(seznam[prvek])
    #print(delka_prvku)
    if delka_prvku > 0:
        soucet_cisel = soucet_cisel + int(seznam[prvek])
        #print(soucet_cisel)

    else:
        seznam_souctu.append(soucet_cisel)
        soucet_cisel = 0
    
# !! v seznamu chybel soucet poslednich prvků, protoze za nimi uz nebyl prazdny radek, takze neprobehl else a nepridalo se do seznamu -> jednoduse vyreseno pridanim prazdneho radku do dat 
print(seznam_souctu)

seznam_souctu.sort()
seznam_souctu.reverse()
print(seznam_souctu)

tri_nejvetsi = seznam_souctu[0] + seznam_souctu[1] + seznam_souctu[2]
print(tri_nejvetsi)