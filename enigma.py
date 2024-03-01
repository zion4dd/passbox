class Enigma:
    @staticmethod
    def control(pin: str) -> str:
        "generates CONTROL using pin"

        # Put your algorithm here
        # Example:
        # if pin.isdigit():
        #     pin = str(int(pin) + 1234)

        return pin

    @staticmethod
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
