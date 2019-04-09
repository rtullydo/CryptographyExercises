# Jenna Uba April 2, 2019
# This program implements the double and add algorithm

# Function One: This is the double and add algorithm which uses the binary expansion of N and the point P to efficiently
# compute nP


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
    if int(P[0]) == 0 and int(P[1]) == 0 and int(Q[0]) == 0 and int(Q[1]) == 0:
        r = [0, 0]
    elif Q == P:
        line = ((3 * (int(P[0])**2)) + A) / (2 * int(P[1]))
        line = int(fast_inverse(1/line, p))
        print(line)
        x = int((line**2) - int(P[0]) - int(Q[0])) % p
        y = int(line * (int(P[0]) - x) - int(P[1])) % p
        r.append(x)
        r.append(y)
    elif int(Q[0]) == int(P[0]) and int(P[1]) == -int(Q[1]):
        r.append(0)
        r.append(0)
    elif int(Q[0]) == 0 and int(Q[1]) == 0:
        r = P
    elif int(P[0]) == 0 and int(P[1]) == 0:
        r = Q
    else:
        line = (int(Q[1]) - int(P[1])) / (int(Q[0]) - int(P[0]))
        line = int(fast_inverse(1 / line, p))
        x = ((line ** 2) - int(P[0]) - int(Q[0]))
        y = (line * (int(P[0]) - x) - int(P[1]))
        r.append(int(x) % p)
        r.append(int(y) % p)
    return r


# Function One: This is the double and add algorithm which uses the binary expansion of N and the point P to efficiently
# compute nP


def fast_multiply(p, N, P, A_val):
    power_bin = format(N, "b")
    binary = power_bin[::-1]
    print(binary)
    a = []
    b = []
    A = int(P[0])
    B = int(P[1])
    for i in range(0, len(binary)):
       a.append(elliptic_add(p, P, P, A_val)[0])
       b.append(elliptic_add(p, P, P, A_val)[1])
       # A *= 2
       # B *= 2
       # a.append(A)
       # b.append(B)
    print(A)
    nP = [sum([i * N for i in a]) % p, sum([i * N for i in b]) % p]
    return nP


# Function Four:  This is where inputs are taken from the user including point P and N, as well as the prime
# number Then another function is called to compute the double and add


def run():
    p_str = input("Please enter point P coordinates in form Px Py: ")
    p_list = p_str.split()
    n_val = int(input("Please enter N: "))
    prime = int(input("Please enter the prime number: "))
    curve = int(input("Enter A Coefficient of the Elliptic Curve: "))
    print(fast_multiply(prime,  n_val, p_list, curve))


run()