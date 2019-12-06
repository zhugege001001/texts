import os

# 本方法是创建一个文件夹
from pip._vendor.distlib.compat import raw_input

file = "新建文件夹"#文件夹名字
url = '123.txt'#文件的名字


#是否存在一个文件路径，如果不存在的话就创建一个
if not os.path.exists(file ):
    os.makedirs(file )
    print('文件不存在，创建')

# 开始创建一个文本文件
f = open("d:\\aaa\\bbbb\\" + url,'w')
# f = open(url,'r')#r模式是读的意思read，a是往后添加
f.write(url)



