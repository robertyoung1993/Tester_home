"""
用于判断质数
"""

class DefinePrime():
    def __init__(self, num):
        self.num = num

    def is_prime(self):
        if self.num <= 1:
            return False
        for i in range(2, self.num):
            if self.num % i == 0:
                return False
        return True