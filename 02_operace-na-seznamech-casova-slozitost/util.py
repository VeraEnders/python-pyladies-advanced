import random
import time

# Napsat funkci, ktera vyrobi seznam dane delky a zamicha ho.
# pouzij range a shuffle
# vrat list

def vytvor_nahodny_seznam(delka):
    seznam = []
    for _ in range(delka):
        new_num = random.randint(0, 9)
        seznam.append(new_num)
    return seznam

def vytvor_seznam(delka):
    seznam = list(range(delka))
    random.shuffle(seznam)
    return seznam

# print(vytvor_nahodny_seznam(10))
# print(vytvor_seznam(10))


def test_time(function, repeat=1):
    times = {}
    for length in range(1000, 10000, 1000):
        t = 0
        for _ in range(repeat):
            my_list = vytvor_seznam(length)
            start = time.time()
            result = function(my_list)
            end = time.time()
            t += end-start 
        print(f"Time for length {length} is {t:.6f} seconds")
        times[length] = t
    print()
    return times