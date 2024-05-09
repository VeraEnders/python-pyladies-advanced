from random import randrange
from pprint import pprint
from time import time

# Napište funkci, která dostane na vstupu řetězec a vrátí slovník četností výskytů jednotlivých písmen.

retezec = 'skakal pes pres oves'

def vygeneruj_retezec(delka):
    ABECEDA = 'abcdefghijklmnopqrstuvwxyz'
    ABECEDA += ABECEDA.upper()
    ABECEDA += '0123456789'
    vysledek = []
    delka_abecedy = len(ABECEDA)
    for pismeno in range(delka):
        vysledek.append(ABECEDA[randrange(delka_abecedy)])
    return ''.join(vysledek)

def read_bible_lines(num=10):
    text = ""
    with open("book_part1.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i > num:
                return text
            text += line
    return text

def count_letters(input_string):
    result = {}
    for pismeno in input_string:
        if pismeno in result:
            continue
        pocet = input_string.count(pismeno)
        result[pismeno] = pocet
    return result

def count_letters_v2(input_string):
    result = {}
    for pismeno in input_string:
        if pismeno in result:
            result[pismeno] += 1
        else:
            result[pismeno] = 1
    return result

# Ukol - najdi nejcastejsi a nejmene caste pismeno v textu
def najdi_minimum(slovnik):
    min_znak = None
    minimum = None
    for znak in slovnik:
        if minimum is None:
            min_znak = znak
            minimum = slovnik[znak]
        if minimum > slovnik[znak]:
            min_znak = znak
            minimum = slovnik[znak]
    return min_znak

def najdi_maximum(slovnik):
    max_znak = None
    maximum = None
    for znak in slovnik:
        if znak in ' ':
            continue
        if maximum is None:
            max_znak = znak
            maximum = slovnik[znak]
        if maximum < slovnik[znak]:
            max_znak = znak
            maximum = slovnik[znak]
    return max_znak

def count_sequence(input_string, seq_len=2):
    result = {}
    for i in range(len(input_string)-seq_len+1):
        pismena = input_string[i:i+seq_len]
        if pismena in result:
            continue
        pocet = input_string.count(pismena)
        result[pismena] = pocet
    return result

def count_sequence_v2(input_string, seq_len=2):
    result = {}
    for i in range(len(input_string)-seq_len+1):
        pismena = input_string[i:i+seq_len]
        if pismena in result:
            result[pismena] += 1
        else:
            result[pismena] = 1
    return result

retezec = vygeneruj_retezec(100_000)
# retezec = read_bible_lines(10_000)

start = time()

## Pro jeden znak obě funkce fungují stehně rychle
# pocty_znaku = count_letters(retezec) # 0.06
# pocty_znaku = count_letters_v2(retezec) # 0.09

## Pro nahodny retezec delky 100_000 znaku
# pocty_znaku = count_sequence(retezec, seq_len=1) # 0.01097 sekund
# pocty_znaku = count_sequence(retezec, seq_len=2) # 0.19947 sekund
# pocty_znaku = count_sequence(retezec, seq_len=3) # 3.62308 sekund

# pocty_znaku = count_sequence_v2(retezec, seq_len=1) # 0.01495 sekund
# pocty_znaku = count_sequence_v2(retezec, seq_len=2) # 0.02098 sekund
pocty_znaku = count_sequence_v2(retezec, seq_len=3) # 0.02194 sekund

## Pro retezec z textu, delka retezce je cca 1_200_000 znaku
# pocty_znaku = count_sequence(retezec, seq_len=1) # 0.14462 sekund
# pocty_znaku = count_sequence(retezec, seq_len=2) # 0.90356 sekund
# pocty_znaku = count_sequence(retezec, seq_len=3) # 5.88227 sekund

# pocty_znaku = count_sequence_v2(retezec, seq_len=1) # 0.1975 sekund
# pocty_znaku = count_sequence_v2(retezec, seq_len=2) # 0.24734 sekund
# pocty_znaku = count_sequence_v2(retezec, seq_len=3) # 0.25332 sekund

print(pocty_znaku)

stop = time()
celkovy_cas = round(stop - start, 5)
print(celkovy_cas, 'sekund')

print('Nejmene caste pismeno:', najdi_minimum(pocty_znaku))
print('Nejcastejsi pismeno:', najdi_maximum(pocty_znaku))
