# Jenna Uba February 2, 2019
# This program uses the Fast Powering Algorithm in conjunction with the fast inverse function to determine the inverse
# of the inputted values.


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


# Function Two:  This is a function that finds the power by subtracting two from the inputted modulo value. This
# function then calls the fast powering algorithm function to compute the result.


def fast_inverse(a, m):
    p = m - 2
    return fast_powering(a, p, m)


# Function Three:  This is where inputs are taken from the user including the base integer, power integer, and mod
# integer. Then another function is called to compute the exponentiation.


def run():
    value1 = int(input("Please enter the integer whose inverse you want to find: "))
    prime = int(input("Please enter the prime number: "))
    print("The inverse of", value1, "modulo", prime, "is", fast_inverse(value1, prime))


run()
