# zkusebni data
"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

hromada_0 = ["nic"]     # pridana pro vyreseni indexu
hromada_1 = ["Z", "N"]
hromada_2 = ["M", "C", "D"]
hromada_3 = ["P"]
seznam_hromad = [hromada_0, hromada_1, hromada_2, hromada_3]
"""
# data
"""
        [H]     [W] [B]            
    [D] [B]     [L] [G] [N]        
[P] [J] [T]     [M] [R] [D]        
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9 
"""

hromada_0 = ["nic"]
hromada_1 = ["T", "D", "W", "Z", "V", "P"]
hromada_2 = ["L", "S", "W", "V", "F", "J", "D"]
hromada_3 = ["Z", "M", "L", "S", "V", "T", "B", "H"]
hromada_4 = ["R", "S", "J"]
hromada_5 = ["C", "Z", "B", "G", "F", "M", "L", "W"]
hromada_6 = list("QWVHZRGB")
hromada_7 = list("VJPCBDN")
hromada_8 = list("PTBQ")
hromada_9 = list("HGZRC")

seznam_hromad = [hromada_0, hromada_1, hromada_2, hromada_3, hromada_4, hromada_5, hromada_6, hromada_7, hromada_8, hromada_9]

with open("05_data.txt") as soubor:
    obsah = soubor.readlines()
#print(obsah)

def presun(pocet, odkud, kam):
    """Funkce dostane počet položek, odkud a kam je má přemístit a vrátí homady a novym obsahem boxu"""
    presouvane_boxy = []
    for i in range(pocet):
        presouvane_boxy.append(seznam_hromad[odkud].pop())
    #print(f"toto jsou presovane boxy {presouvane_boxy}")
    presouvane_boxy.reverse()
    #print(f"toto jsou otocene {presouvane_boxy}")
    seznam_hromad[kam].extend(presouvane_boxy)
    #print(seznam_hromad[kam])

for radek in obsah:
    radek = radek.rstrip()
    #print(radek)
    move, pocet, z, odkud, do, kam = radek.split(sep=" ")
    #print(pocet, odkud, kam)
    pocet = int(pocet)
    odkud = int(odkud)
    kam = int(kam)
    presun(pocet, odkud, kam)

#print(seznam_hromad)
vysledek = []
for i in range(len(seznam_hromad)):
    vysledek.append((seznam_hromad[i][-1]))
print(vysledek)