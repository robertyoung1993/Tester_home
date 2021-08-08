"""
文件读写:
现代操作系统不允许普通的程序直接操作磁盘，读取文件就是请求操作系统打开一个文件对象，然后通过操作系统提供的接口
从这个文件对象中读取数据(读文件)，或者把数据写入这个文件对象(写文件)
"""

# 读文件
# 要以读文件的模式打开一个文件对象，使用python内置的open()函数，传入文件名和标示符

# 打开一个文件对象
f = open('/Users/yanglun/Downloads/code.txt', 'r')

# print(f)

# 文件打开成功，调用read()方法可以一次读取文件的全部内容，python把内容读到内存，用一个str对象表示：
str_obj = f.read()

# print(str_obj)

# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()

# 整体步骤是： 打开文件 --> 读写文件 --> 关闭文件

# 由于文件读写时都有可能产生IOEerror,一旦出错，后面的f.close()就不会调用。所以为了保证无论是否出错都应该正确的关闭文件，
# 可以使用try...finally来实现

# try:
#     f_obj = open('/Users/yanglun/Downloads/code.txt', 'r')
#     print(f_obj.read())
# except IOError as e:
#     print(e)
# finally:
#     if f_obj:
#         f_obj.close()


# with上下文，with语句会自动帮我们调用close()方法

with open('/Users/yanglun/Downloads/code.txt', 'r') as fbj:
    # print(fbj.read())
    pass

# 和try...finally效果一样，但是代码更简洁，并且不需要调用close()方法
# 调用read()方法会一次性的读取文件的全部内容，如果文件有10G，内存就爆掉了，可以反复调用read(size)方法，
# 每次最多读取size个字节的内容，调用readline()可以每次读取一行的内容，调用readlines()一次读取所有内容，并且按照行返回
# 如果文件很小，read()一次性读取最方便，如果不能确定大小，反复调用read(size)比较方便，如果是配置文件，调用readlines()最方便

    for line in fbj.readlines():
        print(line.strip())    # 去掉末尾的换行 '\n'


# 二进制文件
# 前面讲的默认都是读取文本文件，并且都是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等，用'rb'模式打开文件即可

with open('/Users/yanglun/Downloads/video/startbucks-mp4-2.mp4', 'rb') as f_o:
    f_o.read()

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件

# with open('/Users/yanglun/Downloads/穿越时空的爱恋.txt', 'r', encoding='gbk') as f_q:
#     f_q.read()

# 写文件
# 使用write()来反复写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放入内存
# 缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
with open('/Users/yanglun/Downloads/code.txt', 'w') as f_o:
    f_o.write('/Users/yanglun/PycharmProjects/Tester_home/Basing/')

















































