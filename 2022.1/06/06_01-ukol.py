# zkusebni data
#obsah = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

with open("06_data.txt") as soubor:
    obsah = soubor.read()
#print(obsah)

ctverice = ""
for i in range(len(obsah)):
    ctverice = obsah[i:i+4]
    pocet_pismen = 0
    for pismeno in ctverice:
        pocet_pismen = pocet_pismen + ctverice.count(pismeno)       # vyuziti pocitani vyskytu pismen v retezci. pokud je tam pismeno vickrat, tak se ten pocet znasobi. Takze pokud je tam kazde pismeno prave jednou bude pocet roven 4
    if pocet_pismen == 4:
        print(f" ctverice je {ctverice}, hledane cislo {i +4}")
        break



## Reseni od Lumira, za pouziti mnoziny
# for i in range(len(obsah)):
#     if len(set(obsah[i:i+4])) == 4:
#         print(i + 1 + 3)
#         break
    

