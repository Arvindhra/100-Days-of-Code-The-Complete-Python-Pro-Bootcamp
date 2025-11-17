from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# This code was written before optimisation was done. The optimised code would be available
# in the optimized code Python file.

def encrypt(original_text,shift_amount):
  encrypted_text = ''
  for letter in original_text:
    if letter in alphabet:
      initial_letter_index = alphabet.index(letter)
      shifted_letter_index = (initial_letter_index + shift_amount) % len(alphabet)
      encrypted_text += alphabet[shifted_letter_index]
    else:
        encrypted_text += letter
  return encrypted_text

def decrypt(original_text,shift_amount):
  decrypted_text = ''
  for letter in original_text:
    if letter in alphabet:
      initial_letter_index = alphabet.index(letter)
      shifted_letter_index = (initial_letter_index - shift_amount) % len(alphabet)
      decrypted_text += alphabet[shifted_letter_index]
    else:
        decrypted_text += letter
  return decrypted_text


def caesar(encode_or_decode,original_text,shift_amount):
  if encode_or_decode == 'encode':
    encrypted_result = encrypt(original_text, shift_amount)
    print (f"Your encoded text is {encrypted_result}.")
  elif encode_or_decode == 'decode':
    decrypted_result = decrypt(original_text,shift_amount)
    print (f"Your decoded text is {decrypted_result}.")
  else:
    print("Wrong input. You should only type encode or decode to either encrypt or decode the message.")


play_again = True

while play_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)

    encode_or_decode_again = input("\nDo you want to encode/decode again? (yes/no) : \n").lower()

    if encode_or_decode_again == 'no':
        print("Goodbye. See you again next time")
        break