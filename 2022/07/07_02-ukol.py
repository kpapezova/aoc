from collections import defaultdict

with open("07_data.txt") as soubor:
    obsah = soubor.readlines()

#print(obsah)
# vytvorim hlavni adresar, neboli hlavni seznam, do ktereho budu pridavat a odebirat, abych mela aktualni pozici slozky
hlavni_adresar = []

# struktura - slozka jako klic a to co je v ni, jako hodnota (seznam hodnot)
struktura = defaultdict(list)

for i in range(len(obsah)):
    obsah[i] = obsah[i].rstrip()
    radek = obsah[i]

    if radek[0:4] == "$ cd":
        znak, pokyn, nazev = radek.split(" ")
        if nazev == "/":
            print("toto je hlavni adresar /, do ktereho se budou pridavat soubory a dalsi adresare")
            #hlavni_adresar.append(nazev)
        elif nazev == "..":
            hlavni_adresar.pop()
        else:       # napr. cd a, cd d,
            hlavni_adresar.append(nazev)

    elif radek[0:4] == "$ ls":
        pass

    elif radek[0:3] == "dir":
        prikaz, nazev_slozky = radek.split(" ")
        #struktura[nazev].append(nazev_slozky)      nestaci, potrebuji znat cestu
        struktura["/".join(hlavni_adresar)].append(("/".join(hlavni_adresar))+"/"+nazev_slozky)

    else:                # pro radky zacinajici cislem
        velikost, jmeno_souboru = radek.split(" ")
        #struktura[nazev].append(velikost)      nestaci, potrebuji znat cestu
        struktura["/".join(hlavni_adresar)].append(int(velikost))

print("vysledna struktura", struktura)
print("kopie", struktura.copy())

def vypocitej_velikost(i, struktura):
    velikost = 0
    for hodnota in struktura[i]:        # i je klic a for cyklem budu vypisovat hodnoty 
        if type(hodnota) == int:
            velikost += hodnota
        else:
            #pass
            #print(hodnota)
            velikost += vypocitej_velikost(hodnota, struktura)      # pokud je ve slozce slozka, zavola se fce znovu
    
    return velikost

total = 0
for i in struktura.copy().keys():       #musela jsem udelat kopii slovniku struktura, protoze to hazelo RuntimeError: dictionary changed size during iteration
    velikost = vypocitej_velikost(i, struktura)
    # if velikost <= 100000:
    total += velikost

celkove_misto = 70000000
potrebne_misto = 30000000
obsazene_misto = total      # pro vypocet celkoveho obsazeneho mista jsem ve funkci pro else nastavila pass (aby se podslozky nezapocitavaly vickrat )
print(f"obsazeno je {obsazene_misto}")      # 42080344

vysledek = []

for i in struktura.copy().keys():
    velikost = vypocitej_velikost(i, struktura)
    #if celkove_misto - obsazene_misto + velikost > potrebne_misto:
    if celkove_misto - 42080344 + velikost > potrebne_misto:        #obsazene misto zadano rucne
        vysledek.append((i, velikost))

# # vysledek ;)
print(sorted(vysledek, key=lambda x:x[1])[0])
# x:x[1] znamena, ze chci radit podle toho co je na pozici 1, tedy cislo zde
# ta nula nakonci [0] znamena, ze chci vypsat to co je na nultem indexu v tom serazenem seznamu
# ('ldqc/jclb/pbb/zmflq/lcgv/mzzpfnr', 2086088)


## zkousim si
print(sorted(vysledek, key=lambda x:x[1])[1])
print(sorted(vysledek, key=lambda x:x[1])[:2])
print(sorted(vysledek, key=lambda x:x[1])[3]) 
#print(sorted(vysledek, key=lambda x:x[2])[0])       # [2] tuple index out of range


# POZNAMKY
# print(f"celkova velikost vsech souboru {total}")
# volne_misto = celkove_misto  - obsazene_misto          # ukazkovy pr. 48 381 165
# print(f"volne misto je {volne_misto}")      # ukazkovy priklad 21 618 835    mam toto volne misto
# # potrebuji 30 000 000
# min_na_smazani = potrebne_misto - volne_misto     # potrebuji smazat minimalne toto min_na_smazani
# print(f"minimalni velikost na smazani je {min_na_smazani}")