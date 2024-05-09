from util import test_time

test_time(lambda seznam: 0 in seznam, repeat = 100) # linearni

test_time(lambda seznam: len(seznam), repeat = 100) # konstantni


test_time(lambda seznam: seznam.append(5), repeat = 100) # konstantni

test_time(lambda seznam: seznam.index(5), repeat = 100) # linearni

# test_time(lambda seznam: seznam.remove(seznam[0]), repeat = 100) # linearni
def smaz(seznam):
    del seznam[0]

test_time(smaz, repeat = 100) # linearni

