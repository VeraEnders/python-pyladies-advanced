from utils import vypis_cas

slova = set()

with open("book_part1.txt", "r", encoding="utf-8") as f:
    for radek in f:
        radek_slova = radek.strip().split()
        for slovo in radek_slova:
            slova.add(slovo)

slova = list(slova)

print(len(slova))
slova = sorted(slova)

print(slova[:10])

def moje_funkce():
    return "the" in slova

print(vypis_cas(moje_funkce))
print(vypis_cas(lambda: "the" in slova))

def otestuj(slovo, seznam):
    """ Funkce vraci True pokud je slovo v seznamu,
    False jinak. Funkce ocekava setrideny seznam. """
    zacatek = 0
    konec = len(seznam)
    while konec>zacatek:
        delka = konec - zacatek
        stred = zacatek + delka//2
        if seznam[stred] == slovo:
            return True
        elif seznam[stred] > slovo:
            # hledam v prvni pulce
            konec = stred
        else:
            # hledam v druhe pulce
            zacatek = stred+1
    return False

print("Testuji vlastni funkci 'the':", vypis_cas(lambda: otestuj("the", slova)))
slovo = "Asterix" 
print(f"Testuji vlastni funkci '{slovo}':", vypis_cas(lambda: otestuj(slovo, slova)))

mnozina = set(slova)

slovo = "god" 
print(f"Testuji mnozinu '{slovo}':", vypis_cas(lambda: slovo in mnozina))

slovo = "Asterix" 
print(f"Testuji mnozinu '{slovo}':", vypis_cas(lambda: slovo in mnozina))
