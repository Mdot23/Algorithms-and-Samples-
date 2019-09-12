import os 
import base64
from cryptography.fernet import Fernet 
from functools import wraps



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Input 
string_input = input("enter a string: ")

input_length = len(string_input)

output = ""

# For loop to loop the input length and itterate over value
for i in range(input_length):
    character = string_input[i]
    location = alphabet.find(character)
    replace = location +3;
    output += alphabet[replace]

print("Encrypted: ", output)



