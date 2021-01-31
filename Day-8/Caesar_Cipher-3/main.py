alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(direction, text, shift):
    new_text = ""
    for letter in text:
        new_position = -1
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = (position+shift) % 26
        elif direction == "decode":
            new_position = (position - shift) % 26
        new_text += alphabet[new_position]

    print(f"The decoded text is {new_text}")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


caesar(direction, text, shift)
