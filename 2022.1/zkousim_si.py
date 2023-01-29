import string
abeceda = list(string.ascii_lowercase) + list(string.ascii_uppercase)
print(abeceda)

body = 0

for poradi, pismeno in enumerate(abeceda, start=1):
    print(f"{poradi}. {pismeno}")
    #vyhodnot(pismeno)

    
    if pismeno == "a":
        body = body + poradi
    elif pismeno == "Z":
        body = body + poradi
    
print(body)

# zvolat funkci def vyhodnot(znak)