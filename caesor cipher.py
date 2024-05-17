def caesar_cipher(text, shift, mode):
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  result = ''
  for char in text:
    if char.isalpha():
      index = alphabet.find(char)
      new_char = shifted_alphabet[index]
    else:
      new_char = char
    result += new_char
  return result
message = input("Enter your message: ")
shift_value = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
mode = input("Enter 'encrypt' or 'decrypt': ")
if mode not in ["encrypt", "decrypt"]:
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()
if mode == "encrypt":
  encrypted_text = caesar_cipher(message, shift_value, mode)
  print("Encrypted message:", encrypted_text)
else:
  decrypted_text = caesar_cipher(message, shift_value, mode)
  print("Decrypted message:", decrypted_text)
