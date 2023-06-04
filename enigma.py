class Enigma:
    @staticmethod
    def control(pin:str) -> str:
        "generates CONTROL using pin"
        
        # Put your algorithm here

        return pin
    
    @staticmethod
    def crypt_word(inword:str, key:str) -> str:
        "crypt/encrypt word using key"
        key = 'somekey' if not key else key
        
        # Put your algorithm here

        return inword
    
