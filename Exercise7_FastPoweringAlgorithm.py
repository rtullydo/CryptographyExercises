# Jenna Uba February 2, 2019
# This program uses the Fast Powering Algorithm to compute the moded exponentiation of two integers.
# The algorithm uses the bin() function to convert an integer to a binary value.


# Function One: This is a function that calculates that converts the power value into a binary (represented as a string
# for comparison purposes. It then uses this binary value to help efficiently compute the moded exponent expression


def fast_powering(b, p, m):
    power_bin = str(bin(p)[:1:-1])
    multipliers = []
    answer = 1
    for digit in range(0, len(power_bin)):
        if power_bin[digit] == '1':
            calculation = (b**(2**digit)) % m
            multipliers.append(calculation)
    for value in range(0, len(multipliers)):
        answer *= multipliers[value]

    return answer % m


# Function Two:  This is where inputs are taken from the user including the base integer, power integer, and mod
# integer. Then another function is called to compute the exponentiation.


def run():
    base = int(input("Please enter the base integer: "))
    power = int(input("Please enter the power integer: "))
    modulo = int(input("Please enter the modulo integer: "))
    print(base, "to the power of", power, "%", modulo, "=", fast_powering(base, power, modulo))


run()
