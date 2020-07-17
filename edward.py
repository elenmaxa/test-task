import re
import sys


def decrypt_message(text_file):
    with open(text_file, 'r') as file:
        encrypted_message = file.read()
    decrypted_message = re.sub(r'([a-z])\1', r'', encrypted_message)
    return decrypted_message


print(decrypt_message(sys.argv[1]))
