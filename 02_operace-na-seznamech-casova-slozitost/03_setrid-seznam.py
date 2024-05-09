from util import vytvor_seznam, test_time

seznam = vytvor_seznam(20)
print(seznam)

def setrid(seznam):
    for i in range(0, len(seznam)):
        minimum = seznam[i]
        index_min = i
        for j in range(i+1, len(seznam)):
            if seznam[j] < minimum:
                minimum = seznam[j]
                index_min = j

        seznam[i], seznam[index_min] = seznam[index_min], seznam[i]
    return seznam

setrid(seznam)
print(seznam)

# print(minimum)
# print(index_min)

vysledek = test_time(setrid)
print(vysledek)

import matplotlib.pyplot as plt
# plt.plot(vysledek.keys(), vysledek.values(), "o-")

vysledek2 = test_time(sorted)
plt.plot(vysledek2.keys(), vysledek2.values(), "o-")

plt.show()
