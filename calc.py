dct = {
    "en":{ 
        "n1":"Enter first number",
        "n2":"Enter second number",
        "res":"Result is",
    },
    "sr":{ 
        "n1":"Unesite prvi broj",
        "n2":"Unesite drugi broj",
        "res":"Rezultat je"
    }
} 

keys = tuple(dct.keys())
while True:
    lang = input(f"Enter language {keys}:")
    if lang not in dct:
        print("Invalid language")
        continue
    else:
        break

loc = dct[lang];

n1 = int(input(loc["n1"]+": ")) 
n2 = int(input(loc["n2"]+": "))
print(loc["res"]+": ",n1+n2)

