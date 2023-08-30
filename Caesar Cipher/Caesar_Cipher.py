# Caesar Cipher Game
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from caesar_cipher_art import logo
print(logo)

def caesar(start_text, shift_amount, direction_value):
    after_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction_value == "decode":
                new_position = (position - shift_amount)%26
                after_text += alphabet[new_position]
            else:
                new_position = (position + shift_amount)%26
                after_text += alphabet[new_position]
        else:
            after_text += letter
    print(f"The {direction_value}d text is {after_text}.")


end_game = True
while end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, direction_value=direction)

    restart = input("Type 'yes' if you want to start again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        end_game = False
        print("Goodbye.")