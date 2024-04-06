import hashlib


def hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()


def crypt_word(inword: str, key: str) -> str:
    "crypt/encrypt word using key"
    outword = inword
    key = "somekey" if not key else key

    # Put your algorithm here
    # Example:
    # x = sum([ord(i) for i in key])
    # outword = ''
    # for i in inword:
    #     outword += chr(ord(i) + x)

    return outword
