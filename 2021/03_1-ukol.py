# power consumption 
# gamma rate * epsilon rate = power consumption

seznam = []
pozice_0_pocet_nul = 0
pozice_0_pocet_jednicek = 0
pozice_1_pocet_nul = 0
pozice_1_pocet_jednicek = 0
pozice_2_pocet_nul = 0
pozice_2_pocet_jednicek = 0
pozice_3_pocet_nul = 0
pozice_3_pocet_jednicek = 0
pozice_4_pocet_nul = 0
pozice_4_pocet_jednicek = 0


with open("03_zkusebni_data.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        seznam.append(radek)
        print(seznam)
    
    print(seznam[2], seznam[2][1])

    n = len(seznam)     #delka seznamu (napr. 12)
    for i in range(n):        # n-1 protoze se indexuje od 0, i vyjadruje kolikaty prvek
        for j in range(5):
            if j == 0:
                if seznam[i][j] == "0":
                    print(f"tady je to co resim {seznam[i][j]}")
                    pozice_0_pocet_nul = pozice_0_pocet_nul + 1
                elif seznam[i][j] == "1":
                    pozice_0_pocet_jednicek = pozice_0_pocet_jednicek + 1
                    print("super")

            elif j == 1:
                if seznam[i][j] == "0":
                    pozice_1_pocet_nul = pozice_1_pocet_nul + 1
                elif seznam[i][j] == "1":
                    pozice_1_pocet_jednicek = pozice_1_pocet_jednicek + 1

            elif j == 2:
                if seznam[i][j] == "0":
                    pozice_2_pocet_nul = pozice_2_pocet_nul + 1
                elif seznam[i][j] == "1":
                    pozice_2_pocet_jednicek = pozice_2_pocet_jednicek + 1
            
            elif j == 3:
                if seznam[i][j] == "0":
                    pozice_3_pocet_nul = pozice_3_pocet_nul + 1
                elif seznam[i][j] == "1":
                    pozice_3_pocet_jednicek = pozice_3_pocet_jednicek + 1

            elif j == 4:
                if seznam[i][j] == "0":
                    pozice_4_pocet_nul = pozice_4_pocet_nul + 1
                elif seznam[i][j] == "1":
                    pozice_4_pocet_jednicek = pozice_4_pocet_jednicek + 1


    def vyhodnot(nuly, jednicky):
        if nuly > jednicky:
            return "0"
        else:
            return "1"

    vysledek = ""
    vysledek = vysledek + vyhodnot(pozice_0_pocet_nul, pozice_0_pocet_jednicek)
    vysledek = vysledek + vyhodnot(pozice_1_pocet_nul, pozice_1_pocet_jednicek)
    vysledek = vysledek + vyhodnot(pozice_2_pocet_nul, pozice_2_pocet_jednicek)
    vysledek = vysledek + vyhodnot(pozice_3_pocet_nul, pozice_3_pocet_jednicek)
    vysledek = vysledek + vyhodnot(pozice_4_pocet_nul, pozice_4_pocet_jednicek)
    
    
    print("tady je", vysledek)

    #print(f"nul je {pozice_0_pocet_nul} a jednicek je {pozice_0_pocet_jednicek}")
    #print(f"nul je {pozice_1_pocet_nul} a jednicek je {pozice_1_pocet_jednicek}")
    #print(f"nul je {pozice_2_pocet_nul} a jednicek je {pozice_2_pocet_jednicek}")
    #print(f"nul je {pozice_3_pocet_nul} a jednicek je {pozice_3_pocet_jednicek}")
    #print(f"nul je {pozice_4_pocet_nul} a jednicek je {pozice_4_pocet_jednicek}")