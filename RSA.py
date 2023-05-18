import math
from util import *

class RSA():
    def __init__(self, m):
        self.list_of_primes = generate_primes()
        self.p, self.q = self.generate_p_q()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.public_key = self.get_public_key()
        self.private_key = self.get_private_key()
        self.message = m

    def __str__(self) -> str:
        return f"Message: {self.message}\np: {self.p}\nq: {self.q}\nn: {self.n}\nphi: {self.phi}\nPublic Key: {self.public_key}\nPrivate Key: {self.private_key}"

    def encrypt(self):
        """ Encrypts the message with: m^e mod n"""
        encryptable = self.message
        self.message = quick_pow(self.message, self.public_key, self.n)
        #print(f"Encrypting:\n{encryptable}^{self.public_key} mod {self.n} = {self.message}")
        return self.message
    
    def decrypt(self):
        """Decrypts the message using the Chinese Remainder Theorem."""
        cryptable = self.message
        c1_exp = quick_pow(self.private_key, 1, (self.p - 1))
        c2_exp = quick_pow(self.private_key, 1, (self.q - 1))
        c1 = quick_pow(cryptable, c1_exp, self.n) % self.p
        c2 = quick_pow(cryptable, c2_exp, self.n) % self.q

        x, y =  extended_euclidean(self.p, self.q)
        self.message = ((c1 * y * self.q) + (c2 * x * self.p)) % self.n
        #print(f"Decrypting:\n{c1} * {y} * {self.q} + {c2} * {x} * {self.p} mod {self.n} = {self.message}")
        return self.message
            
    def generate_p_q(self):
        """ Gets a prime number from p and q from the prime list and switches them, if p <= q"""
        p = get_random_prime(self.list_of_primes)
        self.list_of_primes.remove(p)
        q = get_random_prime(self.list_of_primes)
        self.list_of_primes.remove(q)

        if p <= q:
            temp = p
            p = q
            q = temp
        return p, q
    
    def get_public_key(self):
        """ Gets a random prime number from prime list, until if it's a relative prime with phi(n)."""
        while True:
            e = get_random_prime(self.list_of_primes)
            if gcd(e, self.phi) == 1:
                self.list_of_primes.remove(e)
                return e
            
    def get_private_key(self):
        """ Creates private key from phi(n) and public key.\n
        If private key (d) is negative, add modulo (n) until it's positive. """
        ret = extended_euclidean(self.phi, self.public_key)[1]
        while ret <= 0:
            ret += self.phi
        return ret