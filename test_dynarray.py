import unittest
import random
from dynarray import DynArray

class MyTests(unittest.TestCase):
    
    def test_insert(self):
        da = DynArray()
        for i in range(5):
            da.append(i)
        for j in range(10):
            da.insert(random.randint(0,4),random.randint(1,14))
        self.assertEqual(16,da.capacity)
        for j in range(20):
            da.insert(random.randint(0,15),random.randint(0,15))
        self.assertNotEqual(16,da.capacity)

    def test_delete(self):
        da = DynArray()
        for i in range(random.randint(0,500)):
            da.append(i)
        for j in range(random.randint(0,100)):
            da.delete(i)

    

if __name__ == '__main__':
    unittest.main()