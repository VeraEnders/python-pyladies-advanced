import gzip
import time

hesla = []

with gzip.open("enwiki-latest-all-titles-in-ns0.gz", "rt") as f:
    i = 0
    for line in f:
           hesla.append(line.strip())
           i += 1
        #    if i > 1_000_000:
        #     break

print(len(hesla))

s = time.time()
print("PyLadies" in hesla)
e = time.time()
print(e-s)