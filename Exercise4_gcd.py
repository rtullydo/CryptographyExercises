# Jenna Uba February 2, 2019
# This program uses the Euclidean Algorithm to compute the gcd of two inputted numbers.
# The algorithm is implemented using recursion


# Function One: This is a recursive function that calculates the quotient and the remainder of the two inputted integers
# Then the Euclidean Algorithm is used until the num2 in the gcd is equal to 0. Once this base case is reached the
# answer is returned.


def gcd(num1, num2):
    answer = num1
    if num2 != 0:
        q = num1 // num2
        r = num1 % num2
        # print(a, " = ", num2, " * ", q, " + ", r)
        answer = gcd(num2, r)
    return answer


# Function Two:  This is where inputs are taken from the user including both integer values. Then another function is
# called and to computer the gcd of the two values and its results are printed.


def run():
    value1 = int(input("Please enter the two integers you want to find the gcd of.\nInteger 1: "))
    value2 = int(input("Integer 2: "))
    print("The gdc of ", value1, " and ", value2, "is ", gcd(value1, value2))


run()
