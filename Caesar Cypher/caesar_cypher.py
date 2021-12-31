alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    if direction == "encode":
        encrypted = ''
        for i in text:
            position = alphabet.index(i)
            encrypted += alphabet[position + shift]
        print(f"The encoded text is {encrypted}")
    elif direction == "decode":
        decrypted = ''
        for i in text:
            position = alphabet.index(i)
            decrypted += alphabet[position - shift]
        print(f'The decoded text is {decrypted}')


caesar(text, shift, direction)

    



