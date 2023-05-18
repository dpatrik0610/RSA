import unittest
from RSA import RSA

class RSATests(unittest.TestCase):
    def test_decrypt(self):
        expected_message = 507
        for i in  range(50):
            m = 507
            instance = RSA(m)
            instance.encrypt()
            instance.decrypt()
            self.assertEqual(instance.message, expected_message)

if __name__ == '__main__':
    unittest.main()