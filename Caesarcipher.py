def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts the input text using the Caesar Cipher technique.

    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The number of positions to shift the letters.
        direction (str): 'encrypt' or 'decrypt' to specify the operation.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift_amount = shift if direction == 'encrypt' else -shift
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char

    return result

def main():
    text = input("Enter the text to encrypt/decrypt: ")
    shift = int(input("Enter the shift value: "))
    direction = input("Enter 'encrypt' or 'decrypt': ")

    result = caesar_cipher(text, shift, direction)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
