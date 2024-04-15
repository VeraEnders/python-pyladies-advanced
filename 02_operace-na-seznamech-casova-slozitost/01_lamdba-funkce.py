def dvojnasobek(x):
    return x*2

print(dvojnasobek(5))
print(dvojnasobek)

moje_funkce = dvojnasobek
vysledek = moje_funkce(10)
print(vysledek)

def opakuj(funkce):
    for i in range(5):
        funkce()

def pozdrav():
    print("Ahoj PyLadies")

opakuj(pozdrav)

opakuj(lambda: print("Ahoj PyKoucove"))

moje_scitani = lambda a, b: a + b

vysledek_scitani = moje_scitani(2, 5)
print(vysledek_scitani)

seznam_funkci = [
    pozdrav,
    lambda: print("Ahoj!"),
    lambda: print("Hello!")
]

for funkce in seznam_funkci:
    funkce()

operatory = {
    "secti": lambda a,b: a + b,
    "odecti": lambda a,b: a - b,
}

a = 2
b = 3
print(operatory["secti"](a, b))
print(operatory["odecti"](a, b))