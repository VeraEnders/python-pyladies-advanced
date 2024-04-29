import random 
from utils import test_time_mnozina, test_time_seznam, test_time_slovnik 

print("Hledání v množině")
test_time_mnozina(lambda mnozina: -1 in mnozina, repeat=100) 

print()
print("Hledání v seznamu")
test_time_seznam(lambda seznam: -1 in seznam, repeat=100) 

seznam = []
for i in range(100):
    seznam.append(random.randrange(10))

print(len(seznam))

# seznam_unikatni = list(set(seznam))
# print(len(seznam_unikatni))

print()
print("Hledání ve slovníku:")
test_time_slovnik(lambda slovnik: slovnik.get(-1, 0), repeat=100)