# Jenna Uba February 2, 2019
# This program uses the Extended Euclidean Algorithm to compute the gcd of two inputted numbers.


# Function Two: This function calculates the u and v value needed to equate au + bv to the greatest common divisor of
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


# Function Two:  This is where inputs are taken from the user including both integer values. Then another function is
# called and to computer the Extended Euclidean Algorithm of the two values and its results are printed.


def run():
    value1 = int(input("Please enter the two integers you want to find the gcd of.\nInteger 1: "))
    value2 = int(input("Integer 2: "))
    results = extended_euclidean_algorithm(value1, value2)
    print("The linear combination given ", value1, " and ", value2, "is ", "(a *", results[1], ") + (b *",
          results[2], ") = g")
    print("This means the gdc of ", value1, " and ", value2, "is ", results[0])


run()
