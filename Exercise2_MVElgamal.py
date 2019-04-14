# Jenna Uba April 7, 2019
# This program implements the MV Elgamal encryption using the fast inverse, Fast_powering, and fast multiply functions
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


# Function Three: This is the double and add algorithm which uses the binary expansion of N and the point P to
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


# Function Fours: Encrypts the inputted message. R, C1 and C2 are computed and returned.


def encrypt(p, P, M, A, a):
    cipher_m = []
    k = random.randint(1, p)
    R = fast_multiply(p, k, P, a)
    S = fast_multiply(p, k, A, a)
    c1 = (int(S[0]) * int(M[0])) % p
    c2 = (int(S[1]) * int(M[1])) % p
    cipher_m.append(R)
    cipher_m.append(c1)
    cipher_m.append(c2)
    return cipher_m


# Function Five: Decrypts the inputted message. R, C1 and C2 are used to compute the decrypted message


def decrypt(p, M, N, a):
    M1 = M[0:2]
    print(M1)
    C1 = M[2]
    C2 = M[-1]
    T = fast_multiply(p, N, M1, a)
    inverse_M1 = (fast_inverse(int(T[0]), p) * int(C1)) % p
    inverse_M2 = (fast_inverse(int(T[1]), p) * int(C2))
    return inverse_M1, inverse_M2


# Function Six: Determines if the user would like to encrypt or decrypt a message. This is where inputs are taken
# from the user. Depending on the users inputs another function is called and its results are printed.


def run():
    action = input("Choose option 1 or 2\n1. Encrypt\n2. Decrypt\n")
    prime = int(input("Enter Large Prime: "))
    key_private = int(input("Enter Private Key: "))
    curve = input("Enter A and B Coefficients of Elliptic Curve in A B: ")
    val_A = int(curve[0])
    if action == "1":
        p_str = input("Please enter point P coordinates in form Px Py: ")
        p_list = p_str.split()
        message = input("Enter two plaintext messages in form M1 M2: ")
        message_list = message.split()
        public_key = fast_multiply(prime, key_private, p_list, val_A)  # [int(p_list[0]) * key_private, int(p_list[1]) * key_private]
        print("The Encrypted Message is: ", encrypt(prime, p_list, message_list, public_key, val_A))
    else:
        cipher_str = input("Enter Encrypted Message is form R1 R2 C1 C2 : ")
        cipher = cipher_str.split()
        message1, message2 = decrypt(prime, cipher, key_private, val_A)
        print("The Decrypted Message is: ", message1, message2)


run()
