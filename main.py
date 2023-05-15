from RSA import RSA
from util import *
def main():
    m = 20
    e = 47
    p = 257
    q = 631
    msg = RSA(m, e, p, q)
    print(msg, "\n")
    msg.encrypt()
    print(f"Encrypted message: {msg.message}\n")

    print(f"Decrypting: {msg.message}")
    msg.decrypt()
    print(f"Decrypted message: {msg.message}")

if  __name__ == "__main__":
    main()