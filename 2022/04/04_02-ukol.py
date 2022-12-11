
with open("04_data.txt") as soubor:
    obsah = soubor.readlines()
    #print(obsah)

print(obsah)

def rozbal(x, y):
    """Rozbalí jednotlivý balíček po číslech, od x po y zvyšující se o 1"""
    x = int(x)
    y = int(y)
    
    seznam_cisel = []
    for i in range(x, y+1):
        seznam_cisel.append(i)

    return seznam_cisel

def najdi_vsechna_cisla(cast_1, cast_2):
    """Funkce projde zadane casti a zjisti, jestli jsou vsechna cisla z cast_1 v cast_2 a naopak"""
    delka_cast_1 = len(cast_1)
    pocet_stejnych = 0
    
    for i in range(delka_cast_1):
        if cast_1[i] in cast_2:
            pocet_stejnych = pocet_stejnych + 1

    if pocet_stejnych >= 1:
        return 1
    
    return 0

body = 0

for radek in obsah:
    radek = radek.rstrip()
    sektor_1, sektor_2 = radek.split(sep=",")
    #print(sektor_1)
    a, b = sektor_1.split(sep="-")
    m, n = sektor_2.split(sep="-")
    cisla_sektor_1 = rozbal(a, b)
    cisla_sektor_2 = rozbal(m, n)
    cast_1_ve2 = najdi_vsechna_cisla(cisla_sektor_1, cisla_sektor_2)
    cast_2_v1 = najdi_vsechna_cisla(cisla_sektor_2, cisla_sektor_1)
    print("casti", cast_1_ve2, cast_2_v1)
    if cast_2_v1 == 1 and cast_2_v1 ==1:
        body = body + 1
    else:
        body =  body + cast_1_ve2 + cast_2_v1
    print(body)

print("celkove body", body)