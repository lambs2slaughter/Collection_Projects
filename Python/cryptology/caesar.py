import string

plainText = str(input("What is the plain text value? "))
shift = int(input("What is the amount to shift? "))
shift %= 26
    
def caesar(plainText: str, shit: int):
  alphabet = string.ascii_letters
  def shifted_alphabet():
    return alphabet[shift:]+alphabet[:shift]
  print(shifted_alphabet())
caesar(plainText, shift)