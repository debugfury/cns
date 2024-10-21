import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    # Two random prime numbers
    p = 3
    q = 7
    n = p * q
    totient = (p - 1) * (q - 1)
    
    # Public key
    e = 2
    
    # Find e such that gcd(e, totient) = 1
    while e < totient:
        if gcd(e, totient) == 1:
            break
        e += 1

    # Private key
    d = None
    k = 2  # arbitrary value
    d = (1 + (k * totient)) // e  # Use integer division

    # Example message
    msg = 12
    
    # Encrypt the message
    c = pow(msg, e, n)
    
    # Decrypt the message
    m = pow(c, d, n)

    # Output results
    print(f"Message data = {msg}")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = pq = {n}")
    print(f"totient = {totient}")
    print(f"e = {e}")
    print(f"d = {d}")
    print(f"Encrypted data = {c}")
    print(f"Original Message Sent = {m}")

if __name__ == "__main__":
    main()
