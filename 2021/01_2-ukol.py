# ukol secist tri po sobe jdouci cisla (pr. prvni cislo + druhe + treti -> predchozi_tri) o jedno poskocit a secist opet tri cisla (tedy druhe + treti + ctvrte -> nasledujici_tri)
# vyhodnotit: pokud predchozi_tri < nasledujici_tri zapocitat bod 
# vypsat soucet zapocitanych bodu, tedy vsech trojic, ktere jsou vetsi nez trojice pred nimi

predchozi_tri = 0


seznam_cisel = []
seznam_trojic = []

with open("01_1-data.txt", encoding="utf-8", mode="r") as soubor:
    obsah = soubor.readlines()

    for radek in obsah:
        radek = radek.rstrip()
        cislo = int(radek)
        seznam_cisel.append(cislo)
        print(seznam_cisel)

    n = len(seznam_cisel)
    print(n)

    for i in range(n-2):
        trojice = seznam_cisel[i] + seznam_cisel[i+1] + seznam_cisel[i+2]
        seznam_trojic.append(trojice)
        #print(seznam_trojic)


    m = len(seznam_trojic)
    pocet_vetsich = 0

    for j in range(m-1):
        if seznam_trojic[j] < seznam_trojic[j+1]:
            pocet_vetsich = pocet_vetsich + 1

    print(pocet_vetsich)

