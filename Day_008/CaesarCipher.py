import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(start_text, shift_amount):
    cipher_text = ""
    for char in start_text:
        if alphabet.__contains__(char):
            cipher_text += alphabet[alphabet.index(char) + shift_amount]
        else:
            cipher_text += char
    return cipher_text


# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(start_text, shift_amount):
    plain_text = ""
    for char in start_text:
        if alphabet.__contains__(char):
            plain_text += alphabet[alphabet.index(char) - shift_amount]
        else:
            plain_text += char
    return plain_text


while True:
    # Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the
    # correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a
    # message.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    if direction == "encode":
        print(f"Encrypt -> {text} by {shift}: ", encrypt(text, shift))

    if direction == "decode":
        print(f"decrypt -> {text} by {shift}: ", decrypt(text, shift))

    end = input("Do you want to end the program 'yes' or 'no':\n").lower()
    if end == 'yes':
        break
