seznam_dvojic = []

with open("02_data.txt", encoding="utf-8") as soubor:
    #obsah = soubor.read() 
    
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
    print(f"Elf hral {elf}, ja jsem hrala {ja}")
    # vyhodnoceni bodů za zahraný symbol
    # body za zahrany symbol jsou nasledujici: kamen (X) je za 1b, papir(Y) 2b, nuzky(Z) = 3b
    if ja == "X":
        body_za_symbol = body_za_symbol + 1
    elif ja == "Y":
        body_za_symbol = body_za_symbol + 2
    elif ja == "Z":
        body_za_symbol = body_za_symbol + 3
    else:
        print("neco je spatne, nebylo ani X ani Y ani Z")
    # vyhodnocení hry pokud já: výhra 6b, remíza 3b, prohra 0b
    # výhra
    if ja == "X" and elf == "C":
        body_za_hru = body_za_hru + 6
    elif ja == "Y" and elf == "A":
        body_za_hru = body_za_hru + 6
    elif ja == "Z" and elf == "B":
        body_za_hru = body_za_hru + 6
    # remiza
    if ja == "X" and elf == "A":
        body_za_hru = body_za_hru + 3
    elif ja == "Y" and elf == "B":
        body_za_hru = body_za_hru + 3 
    elif ja == "Z" and elf == "C":
        body_za_hru = body_za_hru + 3
    # prohra mě v podstatě nezajímá, protože je za ni 0b

print(f"Body získané za zahraný symbol {body_za_symbol}")
print(f"Body získané za hru {body_za_hru}")

celkove_body = body_za_symbol + body_za_hru
print(celkove_body)
