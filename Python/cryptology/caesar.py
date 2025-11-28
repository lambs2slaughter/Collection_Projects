import string

global_shift = 0
global_plainText = ''
global_alphabet = string.ascii_lowercase

def Caesar(shift, plainText, alphabet):
    def shift_alphabet(alphabet):
        return alphabet[shift:]+alphabet[:shift]
    def encrypt():
        table = map()