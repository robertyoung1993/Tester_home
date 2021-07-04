from unit_demo2 import DefinePrime
import unittest

class Test_prime(unittest.TestCase):
    def setUp(self):
        print("test start!!")

    def test_case(self):
        self.assertTrue(DefinePrime(7).is_prime(), msg="他不是质数")

    def tearDown(self):
        print("test end!!")

if __name__ == '__main__':
    # 建立测试集
    suite = unittest.TestSuite()
    suite.addTest(Test_prime("test_case"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run()