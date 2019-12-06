# __*__coding:utf-8__*__
# 测试网上下载源码第一部分，爬取豆瓣电影html文本
# 学习使用定义

import requests

DOWNLOAD_URL = 'http://movie.douban.com/top250/'


# 定义一个函数，一个参数，用于获得url二进制内容
def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content.decode('utf-8')
    return data


if __name__ == '__main__':
    print(download_page(DOWNLOAD_URL))
    with open('./douban.html', 'w', encoding='utf-8') as fp:
        fp.write(download_page(DOWNLOAD_URL))
