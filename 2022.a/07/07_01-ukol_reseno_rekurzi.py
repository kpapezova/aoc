from collections import defaultdict


with open("07_zkusebni_data.txt") as soubor:
    radek = soubor.readlines()


def pocitej_velikost(soubor, total_size):
    """Funkce která dostane řádek s číslem a pokud bude mensi nez 100000 zavola sama sebe s dalsim radkem, ktere pricte.. """
    #ukonci se v pripade, ze dalsi radek zacina symbolem $ a vrati hodnotu souctu, kterou si zapamatuje
    # nebo je soucet vetsi nez 100000

    if soubor[0:1] == "$":
        print("Už toho bylo dost")

    elif soubor[0:3] == "dir":
        print("jdu na dalsi radek")
        pocitej_velikost(soubor[i+1], total_size)
    
    elif soubor[0:1] in "0123456789":
        velikost, jmeno = soubor.split(" ")
        print("ahoj", velikost, jmeno)
        velikost = int(velikost)      ##ValueError: invalid literal for int() with base 10: ''
        print(type(velikost))
        
        total_size = total_size + int(velikost)
        print(f"celkova velikost {total_size}")
        
        #pocitej_velikost(soubor[i+1], total_size)
      



for i in range(len(radek)):
    radek[i] = radek[i].rstrip()
    print(radek[i])
    #print(f" ahoj {radek[i]}, {radek[i+1]}")
    pocitej_velikost(radek[i], 0)

# radek = "12345 b.txt"
# velikost, jmeno = radek.split(" ")
# print(velikost, type(velikost))
#print(pocitej_velikost(radek, 0))