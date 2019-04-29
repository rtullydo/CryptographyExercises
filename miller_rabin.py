# Jenna Uba April 29, 2019
# This program uses the Extended Euclidean Algorithm and the Miller Rabin Algorithm to determine if a value is either
# prime or composite.


# Function One: This function calculates the u and v value needed to equate au + bv to the greatest common divisor of
# the two values inputted.


def extended_euclidean_algorithm(a, b):
    u = 1
    g = a
    x = 0
    y = b
    while y != 0:
        q = g // y
        t = g % y
        s = u - q * x
        u = x
        g = y
        x = s
        y = t
    v = (g - a * u) // b
    return [g, u, v]


# Function Two: This function checks a series of various conditions to determine if an input value is prime


def miller_rabin(n, a):
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    if 1 < extended_euclidean_algorithm(a, n)[0] < n:
        return True
    m = n - 1
    k, q, r = 0, 0, 0
    composite = True
    if a == 1 % n:
        print("Inconclusive")
        exit(1)
    while composite:
        a = a**q % n
        if a == -1 % n:
            print("inconclusive")
            exit(1)
        q, r = divmod(m, 2)
        if r == 1:
            composite = False
            break
        m = q
        k = k + 1
    return composite


# Function Three:  This is where inputs are taken from the user including both value n and value a. The Miller Rabin
# function is then called and the results are printed.


def run():
    val_n = int(input("Please enter the value n: "))
    val_a = int(input("Please enter the value a: "))
    if miller_rabin(val_n, val_a):
        print("The value", val_n, "is composite")
    else:
        print("The value", val_n, "is prime")


run()
