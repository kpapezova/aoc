seznam_dvojic = []

with open("02_data.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        seznam_dvojic.append(radek)
        print(radek)

print(seznam_dvojic)

body_za_symbol = 0
body_za_hru = 0

# rozbaleni seznamu
for i in range(len(seznam_dvojic)):
    elf, mezera, ja = seznam_dvojic[i]
    #print(f"Elf hral {elf}, ja jsem hrala {ja}")
    # pismena promenne {ja} znamenaji X je prohra, Y je remiza a Z je vyhra
    if ja == "X":
        body_za_hru = body_za_hru + 0
    elif ja == "Y":
        body_za_hru = body_za_hru + 3
    elif ja == "Z":
        body_za_hru = body_za_hru + 6
    else:
        print("neco je spatne, nebylo ani X ani Y ani Z")
    # vyhodnoceni bodů za zahraný symbol
    # body za zahrany symbol jsou nasledujici: kamen je za 1b, papir 2b, nuzky 3b
    # ja prohravam je X
    if ja == "X" and elf == "A":        # tedy ja prohravam a elf ma kamen (A), takze muj symbol musi byt nuzky
        body_za_symbol = body_za_symbol + 3
    elif ja == "X" and elf == "B":        # tedy ja prohravam a elf ma papir (B), takze muj symbol musi byt kamen
        body_za_symbol = body_za_symbol + 1
    elif ja == "X" and elf == "C":        # tedy ja prohravam a elf ma nuzky (C), takze muj symbol musi byt papir
        body_za_symbol = body_za_symbol + 2
    # remiza je Y
    elif ja == "Y" and elf == "A":        # tedy je remiza, elf ma kamen (A), takze ja kamen 
        body_za_symbol = body_za_symbol + 1
    elif ja == "Y" and elf == "B":        # tedy je remiza, elf ma papir (B), takze ja papir 
        body_za_symbol = body_za_symbol + 2
    elif ja == "Y" and elf == "C":         
        body_za_symbol = body_za_symbol + 3
    # ja vyhravam je Z
    elif ja == "Z" and elf == "A":        # ja vyhravam, elf ma kamen (A), takze ja papir
        body_za_symbol = body_za_symbol + 2
    elif ja == "Z" and elf == "B":        
        body_za_symbol = body_za_symbol + 3
    elif ja == "Z" and elf == "C":         
        body_za_symbol = body_za_symbol + 1
    

print(f"Body získané za zahraný symbol {body_za_symbol}")
print(f"Body získané za hru {body_za_hru}")

celkove_body = body_za_symbol + body_za_hru
print(celkove_body)