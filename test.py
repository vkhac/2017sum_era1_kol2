import unittest
import kol2

class MyTest1(unittest.TestCase):

    def setUp(self):
        self.l1 = [1, 1, 1, 1]
        self.d1 = {"Test": [1, 2, 3, 4, 5]}
        
    def test_average(self):
        self.assertEqual(4, kol2.get_sum(self.l1))
        self.assertAlmostEqual(1, kol2.get_average(self.l1))
        
    def test_json(self):
        kol2.export_data('test.json',self.d1)
        d2 = kol2.import_data('test.json')
        
        self.assertEqual(self.d1, d2)
 
 
