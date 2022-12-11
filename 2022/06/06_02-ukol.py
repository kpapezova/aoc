# zkusebni data
#obsah = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

with open("06_data.txt") as soubor:
    obsah = soubor.read()
#print(obsah)

ctrnact_cisel = ""
for i in range(len(obsah)):
    ctrnact_cisel = obsah[i:i+14]
    pocet_pismen = 0
    for pismeno in ctrnact_cisel:
        pocet_pismen = pocet_pismen + ctrnact_cisel.count(pismeno)
    if pocet_pismen == 14:
        print(f" ctverice je {ctrnact_cisel}, hledane cislo {i +14}")
        break



## Reseni od Lumira, za pouziti mnozin
# for i in range(len(obsah)):
#     if len(set(obsah[i:i+14])) == 14:
#         print(i + 1 + 13)
#         break