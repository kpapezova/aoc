
seznam = []

with open("03_data.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        seznam.append(radek)

print(seznam)

n = len(seznam)     #delka seznamu (napr. 12)

listofjednicky = [0] * n
listofnuly = [0] * n

for i in range(n):
    m = len(seznam[i])
    for j in range(m):
        prvek = seznam[i][j]
        if prvek == "0":
            listofnuly[j]=listofnuly[j]+1
        
        elif prvek == "1":
            listofjednicky[j]=listofjednicky[j]+1
            # print(f"index: {j}, pocett jednicek: {listofjednicky[j]}")

gama = ""
delta = ""
for k in range(12):
    if listofnuly[k] > listofjednicky[k]:
        gama=gama+"0"
        delta=delta+"1"

    elif listofjednicky[k] > listofnuly[k]:
        gama=gama+"1"
        delta=delta+"0"
        
print(f"Gama: {gama}")
print(f"Delta: {delta}")

    # print(f"gama: {k}, pocet nul:{gama[k]}")
    # print(f"delta: {k}, pocett jednicek: {delta[k]}")
# print(f"tohle je vysledny pocet nul {slovnik_nul}")


