seznam_radku = []

with open("03_data.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        seznam_radku.append(radek)
        #print(radek)

print(seznam_radku)
seznam_casti_A = []
seznam_casti_B = []
print("ahoj")


# rozdeleni radku na 2 pulky 
for radek in seznam_radku:
    print(radek)
    delka_radku = len(radek)
    print(delka_radku)
    pulka_delky = int(delka_radku / 2)
    cast_A = radek[:pulka_delky]
    cast_B = radek[pulka_delky:]
    print(f"cast A je {cast_A} cast B je {cast_B}")
    seznam_casti_A.append(cast_A)
    seznam_casti_B.append(cast_B)

print(seznam_casti_A)
print(seznam_casti_B)

def vyhodnot_vyskyt(A, B):
    """Funkce dostane první půlku řádku a druhou půlku řádku a vyhodnotí, jaké písmeno je v obou částech a to písmeno vypíše"""
    for i in range(len(A)):

        if A[i] in B:
            return A[i]

seznam_pismen = []  # vytvorim seznam pismen, ktere jsou v obou pulkach

for index in range(len(seznam_casti_A)):
    pismeno = vyhodnot_vyskyt(seznam_casti_A[index], seznam_casti_B[index])
    seznam_pismen.append(pismeno)

print(seznam_pismen)

# ted potrebuji abecedu: mala pismena a-z maji hodnotu 1 - 26, velka pismena A - Z maji hodnotu 27 - 52

import string
abeceda = list(string.ascii_lowercase) + list(string.ascii_uppercase)
#print(abeceda)

body = 0    # to jsou body za kazde pismeno

for p in range(len(seznam_pismen)):
    print(seznam_pismen[p])
    for poradi, pismeno in enumerate(abeceda, start=1):
        print(f"{poradi}. {pismeno}")
        #vyhodnot(pismeno)

        if seznam_pismen[p] == pismeno:
            body = body + poradi

# vysledek :-)
print(body)