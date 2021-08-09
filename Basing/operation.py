"""
操作文件和目录
"""

# python内置的os模块也可以直接调用操作系统提供的接口函数

import os


# 系统名称
# print(os.name)
# print(os.uname())
# 注意uname()函数在windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的

# 环境变量
print(os.environ)     # 返回字典

# 获取某个环境变量的值
print(os.environ.get('PATH'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path中，这一点要注意一下。查看、创建、删除目录可以这么调用
# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print(os.path.join(os.path.abspath('.'), 'testdir'))
new_path = os.path.join(os.path.abspath('.'), 'testdir')

# 然后创建一个新目录
os.mkdir(new_path)

# 删除一个目录
os.rmdir(new_path)

# 把两个路径合成一个时，不要直接拼字符串，而是要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 在linux/Unix/Mac下，os.path.join()返回这样的字符串
# part1/part2
# 而windows会返回这样的字符串
# part1\part2

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而是要通过os.path.split()函数，这样可以把一个路径拆分为两部分，
# 后面一部分总是最后级别的目录或文件名

print(os.path.split('/Users/yanglun/Downloads/code.txt'))

# os.path.splittext()可以直接让你得到文件扩展名
print(os.path.splitext('/Users/yanglun/Downloads/code.txt'))

# 这些合并、拆分路径并不是要求目录和文件要真实存在，他们只对字符串进行操作

# 对文件重命名
# os.rename('/Users/yanglun/Downloads/code.txt', '/Users/yanglun/Downloads/code.py')

# 删除文件
 # os.remove('./file')

# 但是复制文件的函数居然在os模块中是不存在的，原因是复制文件并非由操作系统提供的系统调用。
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，他们可以看作是os模块的补充

# 列出当前目录下的所有目录
print(os.listdir('/Users/yanglun/PycharmProjects/Tester_home'))
l = [x for x in os.listdir('/Users/yanglun/PycharmProjects') if os.path.isdir(x)]
print(l)

# 要列出所有的py文件
print([i for i in os.listdir('.') if os.path.isfile(i) and os.path.splitext(i)[1] == '.py'])














