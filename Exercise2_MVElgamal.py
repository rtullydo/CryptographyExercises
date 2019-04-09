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


# Function Three: This is the double and add algorithm which uses the binary expansion of N and the point P to
# efficiently compute nP


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


# Function Fours: Encrypts the inputted message. R, C1 and C2 are computed and returned.


def encrypt(p, P, M, A, a):
    cipher_m = []
    k = random.randint(1, p)
    R = fast_multiply(p, k, P)
    S = fast_multiply(p, k, A)
    c1 = (int(S[0]) * int(M[0])) % p
    c2 = (int(S[1]) * int(M[1])) % p
    cipher_m.append(R)
    cipher_m.append(c1)
    cipher_m.append(c2)
    return cipher_m


# Function Five: Decrypts the inputted message. R, C1 and C2 are used to compute the decrypted message


def decrypt(p, M, N):
    M1 = M[0:2]
    C1 = M[2]
    C2 = M[-1]
    T = fast_multiply(p, N, M1)
    inverse_M1 = (fast_inverse(int(T[0]), p) * int(C1)) % p
    inverse_M2 = (fast_inverse(int(T[1]), p) * int(C2)) % p
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
        public_key = [int(p_list[0]) * key_private, int(p_list[1]) * key_private]
        print("The Encrypted Message is: ", encrypt(prime, p_list, message_list, public_key, val_A))
    else:
        cipher_str = input("Enter Encrypted Message is form R1 R2 C1 C2 : ")
        cipher = cipher_str.split()
        message1, message2 = decrypt(prime, cipher, key_private)
        print("The Decrypted Message is: ", message1, message2 )


run()
