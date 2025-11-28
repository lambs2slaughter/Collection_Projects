import string

class CaesarCypher:
    def __init__(self, shift, plainText):
        self.plainText = str.lower(plainText)
        self.shift = int()
        self.alphabets = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    def printAlphabets(self):
        print(self.alphabets)