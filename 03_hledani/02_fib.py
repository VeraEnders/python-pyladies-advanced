import time

def fibbonaci(n):
    if n == 0 or n == 1:
        return 1
    return fibbonaci(n-1) + fibbonaci(n-2)

s = time.time()
for i in range(10):
    print(i, ":", fibbonaci(i))

e = time.time()
print(f"Cas rekurze: {e-s}")

# print("sto", fibbonaci(100))

def fibbonaci_cyklem(n):
    if n == 0 or n == 1:
        return 1
    # a ... fibbonaci(i-2)
    # b ... fibbonaci(i-1)
    a, b = 1, 1
    for i in range(1, n):
        f = a + b
        a, b = b, f
    return f

s = time.time()
for i in range(10):
    print(i, ":", fibbonaci_cyklem(i))

e = time.time()
print(f"Cas rekurze: {e-s}")

print("sto", fibbonaci_cyklem(100))