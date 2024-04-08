import hashlib
from random import sample
from string import ascii_letters


def hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()


def crypt_word(inword: str, key: str) -> str:
    "crypt/encrypt word using key"
    key = "".join(sample(ascii_letters, 50)) if not key else key
    outword = inword

    # Put your crypt algorithm here
    # BAD Example:
    # x = sum([ord(i) for i in key]) // len(key)
    # outword = ''.join([chr(ord(i) + x) for i in inword])

    return outword
