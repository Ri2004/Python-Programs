# Caesar Cipher Game
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Import and print the logo from art.py when the program starts.
from caesar_cipher_art import logo
print(logo)

#TODO-10: Combine the encrypt() and decrypt() functions into a single function called caesar().
# if user enter symbols/numbers/spaces
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

# TODO-6: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).


end_game = True
while end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-11: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(start_text=text, shift_amount=shift, direction_value=direction)

    restart = input("Type 'yes' if you want to start again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        end_game = False
        print("Goodbye.")






#TODO-3: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-4: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#TODO-5: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# def encrypt(plain_text, shift_amount):
#    cipher_text = ""                                    # e.g.
#   for letter in plain_text:                           # plain_text = "hello"
#       position = alphabet.index(letter)               # shift = 5
#      new_position = position + shift_amount          # cipher_text = "mjqqt"
#     cipher_text += alphabet[new_position]           # print output: "The encoded text is mjqqt"
#   print(f"The encoded text is {cipher_text}")


# encrypt(plain_text=text, shift_amount=shift)


#TODO-7: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-8: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# def decrypt(cipher_text, shift_amount):
    # plain_text = ""                                   #e.g.
    # for letter in cipher_text:                        #cipher_text = "mjqqt"
    #     position = alphabet.index(letter)             #shift = 5
    #     new_position = position - shift_amount        #plain_text = "hello"
    #     plain_text += alphabet[new_position]          #print output: "The decoded text is hello"
    # print(f"The decoded text is {plain_text}")

# decrypt(cipher_text=text, shift_amount=shift)


#TODO-9: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)
