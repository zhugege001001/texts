# --*-- coding:utf-8--*--
# 2019/11/30

import requests
import os

'''页面下单一影片均由 *.ts 文件 传输，那么方法不外乎两个：
1.直接下载不同的 *.ts 文件，放入同一文件夹，合并，组成合并后的影片；
2.分别下载，本地转码或解码 或 统一下载，再转码或者解码
'''

'''
现在我们先来试压方法一：
'''

download_page = 'https://hong.tianzhen-zuida.com/20191120/14251_45efab86/1000k/hls/9f6df1604c7000000.ts'

'''
https://hong.tianzhen-zuida.com/20191120/14251_45efab86/1000k/hls/9f6df1604c7000001.ts
https://hong.tianzhen-zuida.com/20191120/14251_45efab86/1000k/hls/9f6df1604c7000002.ts
...
https://hong.tianzhen-zuida.com/20191120/14251_45efab86/1000k/hls/9f6df1604c7000149.ts
https://hong.tianzhen-zuida.com/20191120/14251_45efab86/1000k/hls/9f6df1604c7000150.ts
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
html = requests.get(download_page,headers).content

# 创建一个文件夹，存入
file_name = "ts格式文件"
part_name = str(download_page)[-10:]

#是否存在一个文件路径，如果不存在的话就创建一个
if not os.path.exists(file_name):
    os.makedirs(file_name)
    print('文件不存在，创建')

# 开始创建一个文本文件
f = open('d:\\' + part_name,'wb')
# f = open(url,'r')#r模式是读的意思read，a是往后添加
f.write(html)
''' 创建文件夹，怎么创建都不对'''
'''问题解决 : mkdir() 和 makedirs()不同，mkdir()只能在跟目录下已经存在的路径创建路径；makedirs（）可以无中生有'''


# part_name = str(url)[-10:]  # 获取字母串后10位



# def main():
#   url = download_page

# if __name__ == '__main__':
#   main()



