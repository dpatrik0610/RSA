import math
from util import *

class RSA():
    def __init__(self, m, e, p, q, d = 0):
        if p <= q:
            self.p = q
            self.q = p
        else:
            self.p = p
            self.q = q
        
        self.n = p * q
        self.phi = (self.p - 1) * (self.q - 1)
        self.message = m
        self.public_key = e
        if d == 0:
            self.private_key = extended_euclidean(self.phi, self.public_key)[1]
        else:
            self.private_key = d

    def encrypt(self):
        self.message = quick_pow(self.message, self.public_key, self.n)
        #print(f"Encrypting:\n{self.message}^{self.public_key} mod {self.n} = {self.encrypted}")
        return self.message
    
    def decrypt(self):
        cryptable = self.message
        """Decrypts the message using the Chinese Remainder Theorem."""
        c1_exp = self.private_key % (self.p - 1)
        c2_exp = self.private_key % (self.q - 1)
        c1 = quick_pow(cryptable, c1_exp, self.n) % self.p
        c2 = quick_pow(cryptable, c2_exp, self.n) % self.q

        x, y =  extended_euclidean(self.p, self.q)

        self.message = ((c1 * y * self.q) + (c2 * x * self.p)) % self.n
        # print(f"Decrypting:\n{c1} * {x} * {self.q} + {c2} * {y} * {self.p} mod {self.n} = {self.decrypted}")
        return self.message

    def __str__(self) -> str:
        return f"Message: {self.message}\np: {self.p}\nq: {self.q}\nn: {self.n}\nphi: {self.phi}\nPublic Key: {self.public_key}\nPrivate Key: {self.private_key}"