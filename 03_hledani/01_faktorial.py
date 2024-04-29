from utils import vypis_cas

def faktorial(x):
    if x > 1:
        return x*faktorial(x-1)
    else:
        return 1

def faktorial2(x):
    vysledek = 1
    for i in range(2, x+1):
        vysledek *= i
    return vysledek

print(faktorial(3))
print(faktorial(6))

# f = vypis_cas(lambda: faktorial(1000))
# print(f)

f2 = vypis_cas(lambda: faktorial2(1000))
print(f2)