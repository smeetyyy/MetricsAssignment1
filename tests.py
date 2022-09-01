import unittest

def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

class Test(unittest.TestCase):
    def test_string(self):
        a = 'name'
        b = 'name'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = False
        self.assertEqual(a, b)
        
    def test_sum(self):
        a=65
        b=34
        result = sum(a,b)
        self.assertEqual(result, a+b)
        
    def test_sub(self):
        a=43
        b=23
        result = sub(a,b)
        self.assertEqual(result, a-b)

if __name__ == '__main__':
    unittest.main()
