# --*-- encoding:utf-8 --*--
# 爬取小说，独立完成，循序渐进

import requests

url = 'https://www.jx.la/book/11961/6501006.html'


# 第一：定义一个方法，一个参数，用于获得url二进制内容
def download_url(url):
    """获取url地址页面内容"""
    '''这是一个方法，获取每一个输入的参数为 不同的url 的二进制内容'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data





