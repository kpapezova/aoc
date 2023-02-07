
horizontalni_pozice = 0
hloubka = 0


with open("02_1-data.txt", encoding="utf-8") as soubor:
    obsah = soubor.readlines()
    #print(obsah)

    for radek in obsah:
        radek = radek.rstrip()
        #radek = radek.replace(" ", ", ")
        # print(radek)
        smer, hodnota = radek.split()
        print(f"smer je {smer} a posun je {hodnota}")
        hodnota = int(hodnota)

        if smer == "forward":
            horizontalni_pozice = horizontalni_pozice + hodnota
            print(horizontalni_pozice)
        elif smer == "down":
            hloubka = hloubka + hodnota
            print(hloubka)
        elif smer == "up":
            hloubka = hloubka + hodnota*(-1)
            print(hloubka)
        else:
            print("neco je nekde spatne")
    
    print(f"horizontalni pozice je {horizontalni_pozice} a hloubka je {hloubka}")
    vysledne_cislo = horizontalni_pozice * hloubka
    print(vysledne_cislo)
