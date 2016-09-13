from math import log

from primes import factorize

def number_to_english(number, multiplier_names={
        3:  "thousand",
        6:  "million",
        9:  "billion",
        12: "trillion",
        15: "quadrillion",
        18: "quintillion",
        21: "sextillion",
        24: "septillion",
        27: "octillion",
        30: "nonillion",
    }, hundred="hundred", tens=[
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ], singles = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ], negative="negative"):
    if number == 0:
        return singles[0]

    if number < 0:
        return negative + " " + number_to_english(-number)


    output = []

    digits = 3 * int(log(number, 10) / 3)
    while digits:
        sub_number = int(number / (10 ** digits))
        if sub_number:
            output.append(number_to_english(sub_number) + " " + multiplier_names[digits])
            number -= sub_number * (10 ** digits)
        digits -= 3

    if number >= 100:
        sub_number = int(number / 100)
        output.append(number_to_english(sub_number) + " " + hundred)
        number -= sub_number * 100

    partial = ""
    if number >= 20:
        partial = tens[int(number / 10)] + " "
        number -= 10 * int(number / 10)

    if number:
        partial += singles[number]
    if partial:
        output.append(partial)

    if not output and not partial:
        return singles[0]

    return " ".join(output[:-1]) + (" and " if len(output) != 1 else "") + output[-1]

def number_to_base(number, base=10, sub_call=number_to_english, sep=" ", *args, **kwargs):
    return sep.join(sub_call(int(number / (base ** i)) % base, *args, **kwargs) for i in xrange(int(log(number, base)), -1, -1))

def number_to_primes(number, power_formats={
        1: "{0}",
        2: "{0} squared",
        3: "{0} cubed",
    }, power_default="{0} to the power of {1}", sub_call=number_to_english, sep=" times ", *args, **kwargs):
    return sep.join(power_formats.get(p, power_default).format(sub_call(x, *args, **kwargs), sub_call(p, *args, **kwargs)) for x, p in factorize(number))