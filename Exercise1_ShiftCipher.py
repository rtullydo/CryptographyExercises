# Jenna Uba February 2, 2019
# This program uses a shift cipher to encrypt a message that is inputted by a user along with a key.
# The message can also be decrypted given the cipher text and proper key.


# Function One: Encrypts the inputted message. The index of each letter in the message is found within the alphabet.
# Then this index number is increased by the key and modded by 26 to account for wrap around.


def encrypt(k, m):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_m = ""
    for letter in m:
        if letter != " ":
            letter = letter.lower()
            index = 0
            index += (alphabet.find(letter) + k) % 26
            cipher_m += alphabet[index]
        else:
            cipher_m += " "
    return cipher_m


# Function Two: Decrypts the inputted message. The index of each letter in the message is found within the alphabet.
# Then this index number is subtracted by the key and modded by 26 to account for wrap around.

def decrypt(k, c):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_c = ""
    for letter in c:
        if letter != " ":
            letter = letter.lower()
            index = 0
            index += (alphabet.find(letter) - k) % 26
            cipher_c += alphabet[index]
        else:
            cipher_c += " "
    return cipher_c


# Function Three: Determines if the user would like to encrypt or decrypt a message. This is where inputs are taken
# from the user including both the message and the key. Depending on the users inputs another function is called and
# its results are printed.

def run():
    action = input("Choose option 1 or 2\n1. Encrypt\n2. Decrypt\n")
    message = input("Enter Message: ")
    key_str = input("Enter Key: ")
    key = int(key_str)
    if action == "1":
        print("The Encrypted Message is: " + encrypt(key, message))
    else:
        print("The Decrypted Message is: " + decrypt(key, message))


run()
