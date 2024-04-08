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

start = time()
retezec = vygeneruj_retezec(10000)
# retezec = read_bible_lines(10000)
# print(retezec)
# pocty_znaku = count_letters(retezec)
pocty_znaku = count_letters_v2(retezec)
print(pocty_znaku)
print('Nejmene caste pismeno:', najdi_minimum(pocty_znaku))
print('Nejcastejsi pismeno:', najdi_maximum(pocty_znaku))
stop = time()
celkovy_cas = round(stop - start, 5)
print(celkovy_cas, 'sekund')