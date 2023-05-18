from RSA import RSA
from util import *

def main():
    m = 20
    msg = RSA(m)
    print(msg, "\n")
    msg.encrypt()
    print(f"Encrypted message: {msg.message}\n")

    print(f"Decrypting: {msg.message}")
    msg.decrypt()
    print(f"Decrypted message: {msg.message}")

if  __name__ == "__main__":
    main()