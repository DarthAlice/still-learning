 def startCypher()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def encrypt(plain_text, shift_amount):
      cipher_text = ""
      for letter in plain_text:
        position = alphabet.index(letter)
        #the index of LETTER is the position #in ALPHABET
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
      print(f"The encoded message is {cipher_text}")  


    def decrypt(encoded_text, shift_amount):
      decoded_text = ""
      for letter in encoded_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decoded_text += new_letter
      print(f"Your decrypted message is {decoded_text}")  

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift) 

restart = input("Would you like to restart? y/n  ")
if restart == "y":
    startCypher()