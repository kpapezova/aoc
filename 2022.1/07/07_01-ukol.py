# POUČENÍ PRO PŘÍŠTĚ - NEDĚLAT WHILE VE FOR CYKLU!!!
#   akorat jsem se zamotala. Pridavala +1 a -1 na ruzna mista, aby to bralo postupne ty indexy, a aby to nehazelo out of range. 
#   chvili fungovalo, ze se dobre vypisovaly radky (ve spravnem poradi), ale hazelo to chybu out of range. pak jsem toto opravila, pridala pocitani velikosti, a nejak jsem to rozbila, ze to preskakuje radky. 


from collections import defaultdict

#obsah = ["$ cd /", "$ ls", "dir a", "14848514 b.txt", "8504156 c.dat", "dir d", "$ cd a", "$ ls", "dir e", "29116 f"]

with open("07_zkusebni_data.txt") as soubor:
    obsah = soubor.readlines()

#print(obsah)
# vytvorim hlavni adresar, neboli hlavni seznam, do ktereho budu pridavat podseznamy
hlavni_adresar = []
# vytvorim slovnik, kde klic bude nazev slozky (to co je napsane za cd) a hotnota indexu na kterem bude ve slovniku
nazvy_a_indexy = defaultdict(str)
level = -1
velikost_slozek = defaultdict(int)
n = 0

for i in range(len(obsah)):
    i = i + n
    obsah[i] = obsah[i].rstrip()
    radek = obsah[i]

    if radek[0:4] == "$ cd":
        znak, pokyn, nazev = radek.split(" ")
        print(pokyn, nazev)
        if nazev == "/":
            print("toto je hlavni adresar /, do ktereho se budou pridavat soubory a dalsi adresare")
        elif nazev == "..":
            level = level - 1
            print(".. Tady to musim dodelat")
        else:       # napr. cd a, cd d,
            level = level + 1
            nazvy_a_indexy[nazev] = level
            
    elif radek[0:4] == "$ ls":
         print(radek)           # tady to dodelat

    else:
        total_size = 0
        while radek[0:1] != "$":
            radek = radek.rstrip()
            n = n + 1
            if radek[0:3] == "dir":
                prikaz, nazev_slozky = radek.split(" ")
                hlavni_adresar.append(nazev_slozky)
            else:                # pro radky zacinajici cislem
                velikost, jmeno_souboru = radek.split(" ")
                velikost = int(velikost)
                total_size = total_size + velikost
            print(radek)
            
            if total_size < 100000:
                velikost_slozek[nazev] = total_size

            if i+n+1 > len(obsah):
                break
            else:
                radek = obsah[i+n]
        n = n-1

    if i+n+1 > len(obsah):
        break

print(velikost_slozek)
print(hlavni_adresar)
print(nazvy_a_indexy)