# 1. Nacti dve cisla od uzivatele
# 2. Nacti operator (+ / -)
# 3. Napis program, ktery spocte vysledek, pouzij slovnik funkci

operatory = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
}

a = int(input("Zadejte prosim prvni cislo: "))
b = int(input("Zadejte prosim druhe cislo: "))
op = input("Zvolte operator (+, -, *): ")

# if op:
#     print(operatory[op](a, b))
# else:
#     print("Neco je spatne.")

vysledek = operatory[op](a, b)
print(a, op, b, "=", vysledek)