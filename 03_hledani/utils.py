import time
 
def vypis_cas(funkce):
    s = time.time()
    vysledek = funkce()
    e = time.time()
    print(f"Čas na vykonání funkce: {e-s:.6f}")
    return vysledek

def test_time_seznam(function, repeat=1):
    times = {}
    for exponent in range(1, 7):
        length = 10**exponent
        t = 0
        for _ in range(repeat):
            my_list = list(range(length))
            start = time.time()
            result = function(my_list)
            end = time.time()
            t += end-start 
        print(f"Time for length {length} is {t:.6f} seconds")
        times[length] = t
    print()
    return times


def test_time_mnozina(function, repeat=1):
    times = {}
    for exponent in range(1, 7):
        length = 10**exponent
        t = 0
        for _ in range(repeat):
            my_set = set(range(length))
            start = time.time()
            result = function(my_set)
            end = time.time()
            t += end-start 
        print(f"Time for length {length} is {t:.6f} seconds")
        times[length] = t
    print()
    return times


def test_time_slovnik(function, repeat=1):
    times = {}
    for exponent in range(1, 7):
        length = 10**exponent
        t = 0
        for _ in range(repeat):
            my_dict = {i: i**2 for i in range(length)}
            start = time.time()
            result = function(my_dict)
            end = time.time()
            t += end-start 
        print(f"Time for length {length} is {t:.6f} seconds")
        times[length] = t
    print()
    return times