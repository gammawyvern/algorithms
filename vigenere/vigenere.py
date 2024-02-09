import numpy as np;
import sys;

########################################
# Encrypt / Decrypt functions
########################################

def encrypt(plain_text, key):
    cipher_text = ""; 

    for index, letter in enumerate(plain_text):
        x = ord(letter) - ord('a');
        y = ord(key[index % len(key)]) - ord('a');
        cipher_text += chr(((x + y) % 26) + ord('a'));

    return cipher_text;


def decrypt(cipher_text, key):
    plain_text = ""; 

    for index, letter in enumerate(cipher_text):
        x = ord(letter) - ord('a');
        y = ord(key[index % len(key)]) - ord('a');
        plain_text += chr(((x - y) % 26) + ord('a'));

    return plain_text;

########################################
# Checking inputs and running
########################################

if len(sys.argv) != 4:
    print("Usage: python script.py [option] [text] [key]");
    sys.exit();

op = sys.argv[1].lower();
text = sys.argv[2].lower();
key = sys.argv[3].lower();

if op == "encrypt" or op == "e":
    print(encrypt(text, key));
elif op == "decrypt" or op == "d":
    print(decrypt(text, key));
else:
    print("\nInvalid operation. Use [encrypt | e] or [decrypt | d]\n")

