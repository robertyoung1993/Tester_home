from test_demo1 import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start!")

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

    def test_add3(self):
        j = Count(10, 76)
        self.assertEqual(j.add(), 86)

    def test_add4(self):
        j = Count(42, 76)
        self.assertEqual(j.add(), 118)

    def tearDown(self):
        print("test end!!")

if __name__ == '__main__':
    # unittest.main()
    # 构建测试集
    suit = unittest.TestSuite()
    suit.addTest(TestCount("test_add2"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suit)
