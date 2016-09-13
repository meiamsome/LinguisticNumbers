from math import sqrt

def _prime_generator():
    data = [False, False]
    while True:
        data += [True] * len(data)
        for i in range(len(data) / 2):
            if data[i]:
                for a in range(i**2, len(data), i):
                    data[a] = False
        for i, val in enumerate(data[len(data) / 2:], len(data) / 2):
            if val:
                yield i
                for a in range(i**2, len(data) ,i):
                    data[a] = False

_pg = _prime_generator()
_primes = []

def _new_prime():
    global _primes, _pg
    _primes.append(next(_pg))

def is_prime(number):
    global _primes
    while not _primes or _primes[-1] < number:
        _new_prime()
    return number in _primes

def prime_generator():
    global _primes
    if not _primes:
        _new_prime()
    i = 0
    while True:
        yield _primes[i]
        i += 1
        if i == len(_primes):
            _new_prime()

def factorize(number):
    number = float(number)
    factors = []
    for p in prime_generator():
        count = 0
        while number / p % 1 == 0:
            number /= p
            count += 1
        if count:
            factors.append((p, count))
        if number == 1:
            break
        if p > sqrt(number):
            break
    if number != 1:
        factors.append((int(number), 1))
    return factors