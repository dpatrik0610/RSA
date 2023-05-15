import unittest
from RSA import RSA

class RSATests(unittest.TestCase):
    def setUp(self):
        self.message = 20
        self.public_key = 47
        self.p = 257
        self.q = 631
        self.instance = RSA(self.message, self.public_key, self.p, self.q)

    def test_encrypt(self):
        expected = 77312
        self.instance.encrypt()
        self.assertEqual(self.instance.message, expected)

    def test_decrypt(self):
        expected = 20
        self.instance.encrypt()
        self.instance.decrypt()
        self.assertEqual(self.instance.message, expected)

if __name__ == '__main__':
    unittest.main()