#!/usr/bin/env python

from linguistic_numbers import number_to_english, number_to_base, number_to_primes

def find_fixpoints(func):
    return [i for i in xrange(1, 1000) if func(i) == i]


if __name__ == "__main__":
    # Fix points of English
    print(find_fixpoints(lambda x: len(number_to_english(x).replace(" ", ""))))

    for base in range(2, 11):
        # Number to English base representation,
        func = lambda x: number_to_base(x, base=base)
        fp = find_fixpoints(lambda x: len(func(x).replace(" ", "")))
        print(base, fp, [func(i) for i in fp])

    # Numbers to prime fix points
    # e.g. 60 = 2 * 2 * 3 * 5 -> two squared times three times five
    print(find_fixpoints(lambda x: len(number_to_primes(x).replace(" ", ""))))

    for base in range(2, 11):
        # Number to primes, with each prime represented with a base
        func = lambda x: number_to_primes(x, sub_call=number_to_base, base=base)
        fp = find_fixpoints(lambda x: len(func(x).replace(" ", "")))
        print(base, fp, [func(i) for i in fp])