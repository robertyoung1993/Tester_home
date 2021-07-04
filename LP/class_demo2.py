# 访问的可见性

class Test():

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    # test.__bar()
    # print(test._foo)
    # 'Test' object has no attribute '__bar'

    test._Test__bar()
    print(test._Test__foo)

if __name__ == '__main__':
    main()