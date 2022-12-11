seznam_radku = []

with open("03_data.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        seznam_radku.append(radek)
        #print(radek)
#print(seznam_radku)

def vyhodnot_vyskyt(A, B, C):
    """Funkce dostane první půlku řádku a druhou půlku řádku a vyhodnotí, jaké písmeno je v obou částech a to písmeno vypíše"""
    for i in range(len(A)):

        if A[i] in B and A[i] in C:
            return A[i]

seznam_pismen = []  # vytvorim seznam pismen, ktere jsou v obou pulkach
delka_seznamu = int(len(seznam_radku))
#print(delka_seznamu)

for i in range(int(delka_seznamu/3)):       # deleno 3 abych nebyla mimo rozsah
    n = i * 3   # pro prochazeni trojic
    pismeno = vyhodnot_vyskyt(seznam_radku[n], seznam_radku[n+1], seznam_radku[n+2])
    seznam_pismen.append(pismeno)

print(seznam_pismen)

# ted potrebuji abecedu: mala pismena a-z maji hodnotu 1 - 26, velka pismena A - Z maji hodnotu 27 - 52
import string
abeceda = list(string.ascii_lowercase) + list(string.ascii_uppercase)
#print(abeceda)

body = 0    # to jsou body za kazde pismeno

for p in range(len(seznam_pismen)):
    #print(seznam_pismen[p])
    for poradi, pismeno in enumerate(abeceda, start=1):
        #print(f"{poradi}. {pismeno}")
        #vyhodnot(pismeno)

        if seznam_pismen[p] == pismeno:
            body = body + poradi

# vysledek :-)
print(body)