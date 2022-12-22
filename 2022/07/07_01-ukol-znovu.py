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
        elif nazev == "..":
            hlavni_adresar.pop()
        else:       # napr. cd a, cd d,
            hlavni_adresar.append(nazev)

    elif radek[0:4] == "$ ls":
        pass

    elif radek[0:3] == "dir":
        prikaz, nazev_slozky = radek.split(" ")
        struktura["/".join(hlavni_adresar)].append(("/".join(hlavni_adresar))+"/"+nazev_slozky)

    else:                # pro radky zacinajici cislem
        velikost, jmeno_souboru = radek.split(" ")
        struktura["/".join(hlavni_adresar)].append(int(velikost))

# vytrorena vysledna struktura. Slozky, podslozky,.., soubory a jejich velikosti
print("vysledna struktura", struktura)
print("kopie", struktura.copy())

def vypocitej_velikost(i, struktura):
    velikost = 0
    for hodnota in struktura[i]:        # i je klic a for cyklem budu vypisovat hodnoty 
        if type(hodnota) == int:
            velikost += hodnota
        else:
            velikost += vypocitej_velikost(hodnota, struktura)      # pokud je ve slozce slozka, zavola se fce znovu
    
    return velikost

total = 0
for i in struktura.copy().keys():       #musela jsem udelat kopii slovniku struktura, protoze to hazelo RuntimeError: dictionary changed size during iteration
    velikost = vypocitej_velikost(i, struktura)
    if velikost <= 100000:
        total += velikost

print("struktura", struktura)

# # vysledek ;)
print(f"celkova velikost souboru mensich nez 100000 je {total}")