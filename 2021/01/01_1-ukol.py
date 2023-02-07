# spočítat kolik čísel je větších oproti číslu před ním

predchozi_cislo = 0
pocet_vetsich = 0

with open("01_1-data.txt", encoding="utf-8", mode="r") as soubor:
    obsah = soubor.readlines()

    for radek in obsah:
        radek = radek.rstrip()
        cislo = int(radek)
        if cislo > predchozi_cislo:
            pocet_vetsich = pocet_vetsich + 1 
            predchozi_cislo = cislo
        else:
            predchozi_cislo = cislo
    
    vysledny_pocet = pocet_vetsich - 1  # vysleny pocet cisel, ktere jsou vetsi nez cislo pred nimi. Minus jedna proto, protoze prvni cislo pred sebou zadne cislo nemelo
    print(vysledny_pocet)
        
        
        

