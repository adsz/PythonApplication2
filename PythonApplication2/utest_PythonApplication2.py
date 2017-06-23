import unittest
from PythonApplication2 import dasti 

class TestStringMethods(unittest.TestCase):
    def test_dasti(self):
        self.assertEqual(dasti('Adam'),'Alo Adam')

if __name__ == '__main__':
    unittest.main()