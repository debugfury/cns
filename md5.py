import hashlib

def compute_md5(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the bytes of the input string
    md5_hash.update(input_string.encode('utf-8'))
    
    # Retrieve the hexadecimal representation of the hash
    return md5_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to hash with MD5: ")
    md5_result = compute_md5(user_input)
    print(f"MD5 hash of '{user_input}' is: {md5_result}")
