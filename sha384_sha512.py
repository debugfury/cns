import hashlib

def sha384_hash(input_string):
    # Create a SHA-384 hash object
    sha384 = hashlib.sha384()
    # Update the hash object with the bytes of the input string
    sha384.update(input_string.encode('utf-8'))
    # Return the hexadecimal representation of the digest
    return sha384.hexdigest()

def sha512_hash(input_string):
    # Create a SHA-512 hash object
    sha512 = hashlib.sha512()
    # Update the hash object with the bytes of the input string
    sha512.update(input_string.encode('utf-8'))
    # Return the hexadecimal representation of the digest
    return sha512.hexdigest()

# Example usage
if __name__ == "__main__":
    input_data = "Hello, World!"
    print(f"SHA-384: {sha384_hash(input_data)}")
    print(f"SHA-512: {sha512_hash(input_data)}")
