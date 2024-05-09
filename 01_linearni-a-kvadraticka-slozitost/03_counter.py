from collections import Counter
from random import randrange
from time import time

def vygeneruj_retezec(delka):
    ABECEDA = 'abcdefghijklmnopqrstuvwxyz'
    ABECEDA += ABECEDA.upper()
    ABECEDA += '0123456789'
    vysledek = []
    delka_abecedy = len(ABECEDA)
    for pismeno in range(delka):
        vysledek.append(ABECEDA[randrange(delka_abecedy)])
    return ''.join(vysledek)

retezec = vygeneruj_retezec(100_000)

def read_bible_lines(num=10):
    text = ""
    with open("book_part1.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i > num:
                return text
            text += line
    return text

# retezec = read_bible_lines(10_000)

def generate_two_sequences(string):
    for i in range(len(string) - 1):
        yield string[i:i+2]

def generate_three_sequences(string):
    for i in range(len(string) - 1):
        yield string[i:i+3]

start = time()

# sequences = generate_two_sequences(retezec)
sequences = generate_three_sequences(retezec)
char_counts = Counter(sequences)

# Pro nahodny retezec delky 100_000 znaku
# Pro jedno pismeno:
# char_counts_dict = dict(char_counts) # 0.00496 sekund
# Pro sekvenci dvou pismen:
# char_counts_dict = dict(char_counts) # 0.03542 sekund
# Pro sekvenci tri pismen:
char_counts_dict = dict(char_counts) # 0.38914 sekund


# Pro retezec z textu, delka retezce je cca 1_200_000 znaku
# Pro jedno pismeno:
# char_counts_dict = dict(char_counts) # 0.04126 sekund
# Pro sekvenci dvou pismen:
# char_counts_dict = dict(char_counts) # 0.22314 sekund
# Pro sekvenci tri pismen:
# char_counts_dict = dict(char_counts) # 0.26825 sekund
print(char_counts_dict)

stop = time()
celkovy_cas = round(stop - start, 5)
print(celkovy_cas, 'sekund')