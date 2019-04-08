# Jenna Uba April 2, 2019
# This program implements the double and add algorithm

# Function One: This is the double and add algorithm which uses the binary expansion of N and the point P to efficiently
# compute nP


def fast_multiply(p, N, P):
    power_bin = format(N, "b")
    a = []
    b = []
    A = int(P[0])
    B = int(P[1])
    for _ in range(0, len(power_bin)):
        A *= 2
        B *= 2
        a.append(A)
        b.append(B)
    nP = [sum([i * N for i in a]) % p, sum([i * N for i in b]) % p]
    return nP


# Function Four:  This is where inputs are taken from the user including point P and N, as well as the prime
# number Then another function is called to compute the double and add


def run():
    p_str = input("Please enter point P coordinates in form Px Py: ")
    p_list = p_str.split()
    n_val = int(input("Please enter N: "))
    prime = int(input("Please enter the prime number: "))
    print(fast_multiply(prime,  n_val, p_list))


run()

