# Jenna Uba April 14, 2019
# This program implements the ecdsa digital signature using the fast inverse, Fast_powering, and fast multiply functions
import random


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
    if int(P[0]) == 0 and int(P[1]) == 0 and int(Q[0]) == 0 and int(Q[1]) == 0:
        r = [0, 0]
    elif Q == P:
        line = ((3 * (int(P[0])**2)) + A) * fast_inverse(2 * int(P[1]), p) % p
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
        line = (int(Q[1]) - int(P[1])) * fast_inverse(int(Q[0]) - int(P[0]), p) % p  # / (int(Q[0]) - int(P[0]))
        # line = int(fast_inverse(1 / line, p))
        x = ((line ** 2) - int(P[0]) - int(Q[0]))
        y = (line * (int(P[0]) - x) - int(P[1]))
        r.append(int(x) % p)
        r.append(int(y) % p)
    return r


# Function Four: This is the double and add algorithm which uses the binary expansion of N and the point P to
# efficiently compute nP


def fast_multiply(p, N, P, a_val):
    power_bin = format(N, "b")
    binary = str(power_bin[::-1])
    points = []
    add = []
    temp = P
    for i in range(1, N):
        P = elliptic_add(p, P, temp, a_val)
        points.append(P)
    for digit in range(0, len(binary)):
        if binary[digit] == '1':
            add.append(points[digit])
    nP = add[0]
    for x in range(1, len(add)):
        nP = elliptic_add(p, nP, add[x], a_val)
    return nP


# Function Five: uses the ecdsa algorithm to sign a plaintext document


def ecdsa_sign(P, q, a, p, d, prk):
    k = random.randint(1, q)
    kp = fast_multiply(p, k, P, a)
    # print(kp)
    s1 = kp[0]
    s2 = fast_inverse(k, p) * (d + kp[0] * prk) % q
    signature = [s1, s2]
    return signature


# Function Six: Uses the ecdsa algorithm to verify a signed plaintext document


def ecdsa_verify(d, signature, p, q, P, pbk, a):
    is_true = False
    v1 = fast_inverse(int(signature[1]), p) * d
    v2 = fast_inverse(int(signature[1]), p) * int(signature[0])
    if elliptic_add(p, fast_multiply(p, v1, P, a), fast_multiply(p, v2, pbk, a), a)[0] % q == int(signature[0]):
        is_true = True
    return is_true


# Function Seven: Determines if the user would like to sign or verify a message. This is where inputs are taken
# from the user. Depending on the users inputs another function is called and its results are printed.


def run():
    action = input("Choose option 1 or 2\n1. Sign\n2. Verify\n")
    p_str = input("Please enter point P coordinates in form Px Py: ")
    p_list = p_str.split()
    q_val = int(input("Please enter the order of the large prime: "))
    curve = input("Enter A Coefficient of Elliptic Curve: ")
    val_a = int(curve[0])
    prime = int(input("Enter Large Prime: "))
    document = int(input("Please enter a plaintext document: "))
    if action == "1":
        private_key = int(input("Please enter the private key: "))
        public_key = fast_multiply(prime, private_key, p_list, val_a)
        print("The Document Signature is: ", ecdsa_sign(p_list, q_val, val_a, prime, document, private_key))
    else:
        pub_str = input("Please enter public key in form Px Py: ")
        pub_list = p_str.split()
        dsig = input("Please enter the document signature in form Dx Dy: ")
        print("The Verification is: ", ecdsa_verify(document, dsig, prime, q_val, p_list, pub_list, val_a))


run()
