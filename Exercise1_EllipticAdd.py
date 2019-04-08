# Jenna Uba March 25, 2019
# This program uses the Fast Powering Algorithm in conjunction with the fast inverse function to find the addition of
# two points on an elliptic curve


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

# Function Three:  This is a function that finds the addition of the two points on the elliptic curve. It uses the fast
# inverse function to help compute the answer.


def elliptic_add(p, P, Q, A):
    r = []
    if P != Q and Q != [fast_inverse(int(P[0]), p), fast_inverse(int(P[1]), p)]:
        line = (int(Q[1]) - int(P[1])) / (int(Q[0]) - int(P[0]))
        x = (line**2 - int(P[0]) - int(P[1])) % p
        y = (line * (int(P[0]) - x) - int(P[1])) % p
        r.append(int(x))
        r.append(int(y))
    if Q == P:
        line = ((3 * int(P[0])**2) + A) / 2 * int(P[1])
        x = (line**2 - int(P[0]) - int(Q[0])) % p
        y = (line * (int(P[0]) - x) - int(P[1])) % p
        r.append(x)
        r.append(y)
    if Q == [fast_inverse(int(P[0]), p), fast_inverse(int(P[1]), p)]:
        r.append(0)
        r.append(0)
    if Q == 0:
        r = P
    return r


# Function Four:  This is where inputs are taken from the user including point P and point Q, as well as the prime
# number Then another function is called to compute the elliptic addition.


def run():
    p_str = input("Please enter point P coordinates in form Px Py: ")
    p_list = p_str.split()
    q_str = input("Please enter point P coordinates in form Qx Qy: ")
    q_list = q_str.split()
    a = int(input("Please enter A: "))
    prime = int(input("Please enter the prime number: "))
    output = elliptic_add(prime, p_list, q_list, a)
    print("The addition of (", p_list[0], ",", p_list[1], ") and (", q_list[0], ",", q_list[1], ") is (",
          output[0], ",", output[1], ")")


run()
