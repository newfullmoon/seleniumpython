#coding = utf-8
import os
import unittest
class RinCse(unittest.TestCase):
    def test_case(self):
        path = os.getcwd()
        print(path)
        # case_path = os.path.join(os.getcwd(),'case')
        # print(case_path)
        suite = unittest.defaultTestLoader.discover(path,'first_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()