from unit_demo3 import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test add start!!")

    def test_add(self):
        self.assertEqual(Count(2, 3).add(), 5)

    def test_add2(self):
        self.assertEqual(Count(41, 76).add(), 117)

    def tearDown(self):
        print("test add end!!")

class TestSub(unittest.TestCase):
    def setUp(self):
        print("test sub start!!")

    def test_sub(self):
        self.assertEqual(Count(2, 3).sub(), -1)

    def test_sub2(self):
        self.assertEqual(Count(71, 46).sub(), 25)

    def tearDown(self):
        print("test sub end!!")

if __name__ == '__main__':
    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))

    # 运行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)